## 卸载docker

```bash
# 修改SELINUX=disabled 
sudo sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
sudo dnf remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-engine
```

## 卸载podman和buildah

```bash
sudo dnf remove podman buildah -y
#  podman和buildah与docker的依赖冲突
```

## 安装yum工具包

```bash
sudo dnf config-manager --add-repo="https://download.docker.com/linux/centos/docker-ce.repo"
sudo dnf repolist
sudo dnf makecache
```

## 安装docker

```bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
```

## 设置docker

```bash
sudo usermod -a -G docker {UserName}
```

## 设置开机启动

```bash
sudo systemctl enable docker.service
```

- 青龙

```bash
docker run -dit -v /home/alice/file/data/docker_volume/qinglong/data:/ql/data -p 5700:5700 --name qinglong --hostname qinglong --restart unless-stopped whyour/qinglong:latest
```
