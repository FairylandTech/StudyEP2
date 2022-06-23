[toc]

# AI雷达外推模型部署说明

## 一. 环境部署

### 1. 安装NVIDIA驱动

1) 准备工作

**①GNOME需要安装lightdm** `sudo apt-get install lightdm`

**②安装依赖** `sudo apt-get install gcc g++ make`

**③屏蔽nouveau驱动**

> 步骤一:
>
> `sudo vim /etc/modprobe.d/blacklist-nouveau.conf`
>
> 步骤二:
>
> > 写入 `blacklist nouveau` 和 `options nouveau modeset=0`

- 更新 `sudo update-initramfs -u`
- 重启 `reboot`
- 验证(没有任何输出则正确) `lsmod | grep nouveau`

2修改引导

确保选项NVIDIA GPU和PCIe网络适配器与相应的驱动程序通信 `vim /etc/default/grub`

在"GRUB_CMDLINE_LINUX_DEFAULT="之后，在引号中添加"pci=realloc=off"，如下所示:

![update_grub](static/invdia-driver-statics/update_grub.png)

* 更新grub `sudo update-grub`
* 重启 `reboot`

3) 安装 NVIDIA 驱动

**关闭界面**

```bash
sudo service lightdm stop
```

**官网方式安装**

* [NVIDIA Tesla A100 80G 驱动官网下载](https://www.nvidia.cn/Download/index.aspx?lang=cn)

- 卸载 `sh NVIDIA-Linux-x*.run --uninstall`

**Ubuntu20.04自带驱动安装**

* 查看驱动版本, 并选择需要的版本, 这里选择 nvidia-utils-510-server 版本: `nvidia-smi` 或者 `ubuntu-drivers devices`
  <br/>
  ![nvidia-driver](static/invdia-driver-statics/nvidia-driver.png)
* 安装:

  ```bash
  sudo apt-get update  
  sudo apt-get install nvidia-headless-no-dkms-510-server
  sudo apt-get install nvidia-utils-510-server 
  sudo apt-get install nvidia-dkms-510-server
  ```
* 验证 `nvidia-smi`
* 长时间监控 `watch -n 1 -d nvidia-smi # 1s刷新一次nvidia-smi命令`
* 卸载

  ```bashrc
  sudo apt-get autoremove nvidia-headless-no-dkms-510-server
  sudo apt-get autoremove nvidia-utils-510-server
  sudo apt-get autoremove nvidia-dkms-510-server
  sudo apt-get purge nvidia*
  ```

### 2. 安装CUDA Toolkit

* 查看显卡驱动对应的cuda版本(右上角CUDA Version版本) `nvidia-smi`
  ![nvidia-smi](static/invdia-driver-statics/nvidia-smi.png)
* [官网下载CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive)
* 选择对应cuda版本和系统, 按照官网提供的方式安装
  ![cuda-select](static/invdia-driver-statics/cuda-select.jpg)
  ```bash
  wget https://developer.download.nvidia.com/compute/cuda/11.6.2/local_installers/cuda_11.6.2_510.47.03_linux.run
  sudo sh cuda_11.6.2_510.47.03_linux.run # 记得取消驱动安装, 如果已经安装过驱动了
  ```
* 添加环境变量: `vim /etc/profile # 全局` 或者 `vim ~/.bashrc # 当前用户`
  ```bash
  export PATH=/usr/local/cuda-11.6/bin${PATH:+:${PATH}}  
  export LD_LIBRARY_PATH=/usr/local/cuda-11.6/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
  export CUDA_HOME=/usr/local/cuda
  ```
* 更新 `source /etc/profile` 或 `source ~/.bashrc`
* 验证 `nvcc -V`
  ![nvcc](static/invdia-driver-statics/nvcc.png)
* 卸载:
  ```bash
  cd /usr/local/cuda/bin/
  sudo ./cuda-uninstaller
  ```

### 3. 安装CuDNN

* 查看cuda版本: `nvcc -V` 或 `nvidia-smi`
* [官网下载安装包, 对应cuda版本](https://developer.nvidia.com/rdp/cudnn-download)
  ![cudnn-select](static/invdia-driver-statics/cudnn-select.jpg)
* 解压: `cudnn-linux-x86_64-8.4.0.27_cuda11.6-archive.tar.xz`
* 进入解压目录:
  ```shell
  sudo cd cudnn-linux-x86_64-8.4.0.27_cuda11.6-archive/
  sudo cp include/cudnn.h /usr/local/cuda/include
  sudo cp include/cudnn_version.h /usr/local/cuda/include
  sudo cp lib64/libcudnn* /usr/local/cuda/lib64
  sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/include/cudnn_version.h /usr/local/cuda/lib64/libcudnn*
  ```
* 验证: `cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2`
* 卸载:
  ```shell
  sudo rm -rf /usr/local/cuda/include/cudnn.h
  sudo rm -rf /usr/local/cuda/include/cudnn_version.h
  sudo rm -rf /usr/local/cuda/lib64/libcudnn*
  ```

### 4. 安装Anaconda并创建激活虚拟环境

```bash
## 安装
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.3.1-Linux-x86_64.sh
chmod 755 Anaconda3-5.3.1-Linux-x86_64.sh
./Anaconda3-5.3.1-Linux-x86_64.sh  # 根据提示进行安装
## 环境变量
echo 'export ANACONDA_HOME={Install Path}' >> ~/.bash_profile
echo 'export PATH=$ANACONDA_HOME/bin:$PATH' >> ~/.bash_profile
source ~/.bash_profile
## 检查conda是否安装成功
conda -V
## 激活conda默认环境
source activate  # 这个两个命令都可以
conda activate  # 这个两个命令都可以
## 退出虚拟conda默认环境
source deactivate  # 这个两个命令都可以
conda deactivate  # 这个两个命令都可以
## 创建虚拟环境
conda create -n radar_env python=3.7.9  # 虚拟环境名称为: radar_env
## 激活虚拟环境(radar_env)
source activate radar_env  # 这个两个命令都可以
conda activate radar_env  # 这个两个命令都可以
```

## 二. 项目部署

### 1. 获取设备SN编码并解压项目tar.gz包

```bash
## 获取设备SN编码
# CPU ID
sudo dmidecode -t 4 | grep ID
# 主板序列号
sudo dmidecode -t 2 | grep Serial
sudo cat /sys/class/dmi/id/board_serial
# 硬盘
sudo hdparm -i {Disk Mount Point}
lsblk -dno SERIAL
## 解压项目包
tar -zxvf {Program Name}.tar.gz
```

### 2. 获取KEY文件(重要)

- ①把获取到设备SN编码的信息邮箱发送至(alice_engineer@yeah.net)
- ②替换KEY文件

### 3. 安装项目依赖包(重要)

**在radar_env虚拟环境下**

```bash
pip -V
cat requirements.txt | grep -v torch > requirements_new.txt
pip install -r requirements_new.txt
```

**获取pytorch**

1. 获取CUDA版本
2. 根据CUDA的版本获取[PyTorch](https://pytorch.org), 执行<kbd>Run this Command</kbd>

>**说明**: <font color="red">Package</font>选择<kbd>Pip</kbd>
> 
>安装是若提示找不到pip3, 则用pip代替(pip install .........)

<img src="./static/img/pytorch_install.png" alt="PyTorch_install" title="Image"/>



