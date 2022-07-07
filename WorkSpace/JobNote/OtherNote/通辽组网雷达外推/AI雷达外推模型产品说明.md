[toc]

# AI雷达外推模型

## 1. 产品概述

基于实况雷达回波数据, 对未来1小时天气情况进行预测

## 2. 技术支撑

项目采用生成对抗网络（GAN: Generative Adversarial Network）技术，实现强对流天气的识别，其核心是一个生成网络和一个判别网络，在原始图像A映射时 GA→B 可以产生一个图像XAB ∈ Bfake

生成网络做映射即GA→B(XB)，判别网络D的作用是判断XAB与XB的距离，当距离很大的时候，则认为GA→B不合格，直到D不能判断出两者距离有明显差别。

<img src="https://file.share.alicehome.ltd/pic/markdown/other/png.01.png" alt="png.01" title="Pic">

## 3. 外推检验

将对应的<font color=#ff0000>雷达外推图像</font>与<font color=#ff0000>雷达实测图像</font>做相似性检验
检验对象为≥35dBZ的雷达回波，系统将自动识别 Fcst 和 Obs 中满足该阈值的对象，并分别变化标注在第三组图片中;≥25dBZ 的雷达回波范围将合并显示，如第二组图像中填色区域
右侧表格显示为 Fcst 和 Obs 中，识别对象之间的匹配度，如Fcst中对象21与Obs对象18相似度为98.21%

## 4. 运行环境

- 硬件配置


| 内容        | 配置                                               | 说明                                     |
| ------------- | ---------------------------------------------------- | ------------------------------------------ |
| 操作系统    | Ubuntu18.04LTS/RedHat7.2及以上                     | 需要安装好GNOME                          |
| NVIDIA 显卡 | NVIDIA GeForce RTX 3060(12GB)(消费级显示卡) 及以上 | 需要安装好显卡驱动                       |
| 内存        | 8GB及以上                                          | 推荐16GB+                                |
| CPU         | 4core 2.8GHz及以上                                 | 推荐 3.2GHz                              |
| 硬盘        | 200G及以上(操作系统占用除外)                       | 程序运行过程中会产生一些日志(推荐500GB+) |
| 网卡        | 100Mbps以太网卡及以上                              | 推荐1000Mbps以太网卡                     |

**<font color="red" size="5">注意:</font>**

1. <font color="red">配置显卡时, 按需配置电源</font>

## 5. 数据处理

1) 数据输入

多个雷达基数据解析为图像数据的数据集(一个数据集为20张时间连续且回波较强雷达图像)

2) 数据输出

1小时后雷达预测数据

3) <font color="red">__数据调用__</font>

> <font color="red">数据输入输出均为项目运行服务器的指定路径下</font>

```bash
# 1. 数据输入路径
/home/app/img_src/
# 2. 数据输出路径
/home/app/predict_output/
```

> 输出数据调用方式可以采用SMB/FTP/SFTP/Nginx等

## 6. 安装与部署

1) 部署路径

```bash
/root/radar_extraplation_tongliao_kpl
```

3) 启动方式

```bash
# 1. 激活conda虚拟环境
# 虚拟环境名称--> radar_env
source activate radar_env
# 2. 启动程序
# 2.1 前台启动
python /root/radar_extraplation_tongliao_kpl/run.py
# 2.2 后台无日志启动
python /root/radar_extraplation_tongliao_kpl/run.py
# 2.2 后台指定日志位置启动
python /root/radar_extraplation_tongliao_kpl/run.py >> {logs path} &
```

4) 停止方式

```bash
# 1. 前台Ctrl+c
# 2. 后台启动方式停止
kill $(ps -fe | grep -v grep | grep run.py | awk '{print $2}')
# ** 如有僵尸进程请使用 kill PPID
```

## 7. 维护与管理

1) 日志事件

日志地址

```bash
/root/log/radar_extraplation_tongliao_kpl.log
```

2) 注意事项

1. 确保操作系统永久静止更新
2. 确保操作系统GNOME模式不进行"休眠"
3. 项目启动使用root用户启动
