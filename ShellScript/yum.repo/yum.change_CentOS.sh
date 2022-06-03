#!/bin/bash
#########################################################################
# File Name: yum.change_CentOS
# Author: Alice
# mail: private.profession@foxmail.com
# Created Time: Sun 12 Sep 2021 12:05:36 AM EDT
#########################################################################

echo 'Update Tsinghua Mirrors'
sudo sed -e 's|^mirrorlist=|#mirrorlist=|g' -e 's|^#baseurl=http://mirror.centos.org|baseurl=https://mirrors.tuna.tsinghua.edu.cn|g' -i.bak /etc/yum.repos.d/CentOS-*.repo
yum clean all
yum makecache
echo 'Done!'
echo 'update yum'
yum update -y
echo 'Done!'''
