# Linux运维(基础模块)--day1

## 网络配置

- 修改配置文件

1. nmtui

![umtui](https://pic.amfc.ltd/file/%23Could/Typora/nmtui.png)

2. 修改/etc/sysconfig/network-scripts/ifcfg-ens33配置文件

![网卡](https://pic.amfc.ltd/file/%23Could/Typora/wangka.png)

第一种修改方式:

```shell
# vi /etc/sysconfig/network-scripts/ifcfg-ens33
BOOTPROTO=none/static  # 网卡获取IP的方式
	# none/static-->手动配置IP地址(静态)
	# dhcp-->自动获取IP地址(动态)
ONBOOT=yes  # 是否开机自动启动网卡
	# yes-->开机启动
	# no-->开机禁用
IPADDR=10.1.1.10  # IP地址
PREFIX=16  # 子网掩码 也可以写 NETMASK=255.255.0.0
GATEWAT=10.1.0.1  # 网关
DNS1=114.114.114.114  # DNS,可以写3个
```

------

第二种修改方式:

```shell
# 修改IP
sed -i 's/IPADDR=10.1.1.10/IPADDR=10.1.1.100/g' /etc/sysconfig/network-scripts/ifcfg-ens33
sed -i 's/ONBOOT=no/ONBOOT=yes/g' /etc/sysconfig/network-scripts/ifcfg-ens33
sed -i 's/BOOTPROTO=dhcp/BOOTPROTO=none/g' /etc/sysconfig/network-scripts/ifcfg-ens33
```

- <font color=#ff0000>重启网卡</font>

```shell
# 重启网卡
systemctl restart network
```

## ssh连接优化

- 关闭selinux

```shell
# vi /etc/selinux/config
SELINUX=disabled
```

```shell
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
```

<font color=#ff0000>**修改后必须重启服务器**</font>

```shell
# 重启服务器
shutdown -r now
```

<font color=#ff0000>临时修改--> setenforce 0</font>

- ssh连接失败
  1. 检查ip
  2. 关闭防火墙

```shell
# 临时关闭防火墙
systemctl stop firewall
# 永久关闭防火墙
systemctl disable firewall
```

## 语言支持

```shell
# 查看系统当前语言设置
echo $LANG
# 修改语言
LANG=en_US
# en_US  -->English
# zh_CN.UTD-8  -->Chinese
```

## yum源

<font size=4>**Linux的软件管理工具**</font>

```shell
# yum仓库菜单
ls /etc/yum.repos.d/
```

```shell
# yum仓库源
# cat /etc/yum.repos.d/CentOS-Base.repo
[base]
name=CentOS-$releasever - Base
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
#baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

# [base]  -->仓库名称
# name=  -->仓库描述
# mirrorlist  -->仓库镜像路径
# baseurl  -->仓库url
# enabled  -->仓库是否启用 1: 启用, 0: 关闭
# gpgcheck  -->密钥检测 1: 开启检测, 0: 关闭检测
# gpgkey -->密钥路径
```

<font size=4>**国内常用开源镜像站**</font>

- [阿里云镜像站](https://developer.aliyun.com/mirror/)
- [清华镜像站](https://mirrors.tuna.tsinghua.edu.cn/)
- [中科大镜像站](http://mirrors.ustc.edu.cn/)
- [网易163镜像站](http://mirrors.163.com/)

<font size=4>**构建国内镜像源**</font>

1. 备份本地镜像源
2. 下载或替换国内镜像源
3. 清除yum缓存
4. 生成yum缓存

```shell
# 清除yum缓存
yum clean all
# 生成yum缓存
yum makecache
```

```shell
# yum命令
yum list  # 列出所有yum package
yum search + [command]  # 查找command对应的依赖包
yum install + [package]  # 安装package包
yum remove + [package]  # 卸载package包

yum grouplist  #按组
yum groupinstall
yum groupremove

yum update  # 升级yum
```

##  目录结构

```shell
# tree / -L 1
/
├── bin -> usr/bin  # 所有用户可用的Linux基本命令
├── boot  # 引导加载必须用到的文件(Kernel, initramfs(initrd), grub)等
├── dev  # 特殊文件或设备文件
├── etc  # 系统程序的配置文件
├── home  # 用户的家目录
├── lib -> usr/lib  # 动态链接共享库
├── lib64 -> usr/lib64  # 
├── media  # 系统自动识别的设备, eg: U盘, DVD等
├── mnt  # 为用户提供了临时的文件挂载目录
├── opt  # 为用户提供软件安装的路径, 默认是空的
├── proc  # Linux虚拟文件系统, 内存映射(不在磁盘中)
├── root  # root用户的家目录
├── run  # 临时文件系统
├── sbin -> usr/sbin  # 系统管理使用的工具命令
├── srv  # 用来存放服务启动后需要提取的数据
├── sys  # 系统内核
├── tmp  # 为用户提供来放临时文件
├── usr  # Linux共享资源目录(重要性仅次于根目录)
└── var  # 日志文件目录
```

<font size=4>**开机启动流程**</font>

<kbd>电源</kbd>--><kbd>BIOS硬件自检</kbd>--><kbd>读磁盘</kbd>--><kbd>MBR主引导</kbd>--><kbd>PT分区表</kbd>