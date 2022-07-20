# Linux时区转换CST和同步硬件时间和系统时间

1. 查看系统时间

```shell
date
```

2. 查看硬件时间(BIOS时间)

```shell
hwclock
```

3. 查看本地时区

```shell
ls -all /etc/ | grep localtime
```

如果时区是对的就不用修改时区

<font color=red>对的时区</font>👇👇👇

4. 修改时区

```shell
# 备份原文件
# 直接删除也行(不推荐)  rm -rf /etc/localtime
mv /etc/localtime /etc/localtime.bak
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 查看时区
ls -all /etc/ | grep localtime
```

5. 修改时间

- 不能访问百度

	1. 设置时间日期
	2. 系统时间同步硬件时间

```shell
# date -s 设置的时间为服务器系统时间
date -s "yyyy-MM-dd HH:mm:ss"
# 系统时间同步硬件时间
hwclock -w
# 硬件时间同步系统时间
# hwclock -s
```

- 可以访问百度

	1. 使用ntp ntpdate
	2. 同步时间服务器
	3. 同步硬件时间

```shell
# 下载ntp ntpdate依赖
yum install ntp ntpdate -y
# 时间同步时间服务器

# 系统时间同步硬件时间
hwclock -w
```