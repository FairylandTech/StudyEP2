#!/bin/bash

mkdir -p ~/.config/clash/
cp Country.mmdb ~/.config/clash/
yum install wget -y
wget -O ~/.config/clash/config.yaml $1
gzip -d clash-linux-amd64-v1.10.6.gz
cp clash-linux-amd64-v1.10.6 /usr/local/bin/clash
clash