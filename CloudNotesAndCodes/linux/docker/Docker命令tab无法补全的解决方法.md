# Docker命令tab无法补全的解决方法

## 安装bash-completion

```shell
# 1--
yum install -y bash-completion
```

## 刷新文件

```shell
# 2--
source /usr/share/bash-completion/completions/docker
source /usr/share/bash-completion/bash_completion
```
