# Docker网卡

1. 建立网卡

```shell
docker network create --driver bridge --subnet 111.11.0.0/24 --gateway 111.11.0.1 docker_net
```

