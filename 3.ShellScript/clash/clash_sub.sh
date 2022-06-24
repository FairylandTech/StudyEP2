#!/bin/bash
# 局域网

# 订阅
sub_kk_cloud() {
  echo -e "Start downloads Sub link!"
  wget -O sub.yaml.src "$1"
  cp sub.yaml.src sub.yaml
  sed -i '1i mixed-port: 1080' sub.yaml
  sed -i 's/log-level: info/log-level: debug/g' sub.yaml
  sed -i 's/external-controller: :9090/external-controller: :56011/g' sub.yaml
  sed -i 's/external-controller: 127.0.0.1:9090/external-controller: 0.0.0.0:56011/g' sub.yaml
  cp sub.yaml config.yaml
}

# 重启Clash
restart_clash() {
  if [ "$(netstat -ntlp | grep -c 1080)" == 1 ]; then
    kill "$(pgrep clash | awk '{print $1}')"
    sleep 10
    clash > ~/file/logs/clash.log &
  else
    clash > ~/file/logs/clash.log &
  fi
}

# __main__
cd ~/.config/clash || mkdir -p ~/.config/clash && cd ~/.config/clash || pwd
if [ "$(find ./ -name "Country.mmdb" | wc -l)" == 0 ]; then
  echo -e "State Downloads \"Country.mmdb\" file"
  wget "https://file.share.alicehome.ltd/data/file/clash/Country.mmdb"
  sub_kk_cloud "$1"
  echo -e "Sub successfully. Now, Start Clash... (ps. At least 10s)"
  restart_clash
elif [ "$(find ./ -name "Country.mmdb" | wc -l)" == 1 ]; then
  sub_kk_cloud "$1"
  echo -e "Sub successfully. Now, Start Clash... (ps. At least 10s)"
  restart_clash
else
  echo -e "Please check the path to the \"Country.mmdb\" file"
fi
