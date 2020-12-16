#!/bin/bash

#create_date 2020/11/15
#modify_date 2020/11/15

# by pty
#判断是否为root用户
if [ `whoami` != "root" ];then
    echo " only root can run it"
    exit 1
fi


#########

#设置PS 显示，不然太单调了,最后的\$ 要有个转义\\ $ 
echo "PS1='\[\033[01;35m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\\$ '" >> ~/.bashrc
source ~/.bashrc

#设置 http代理
echo "export http_proxy='http://10.134.99.64:66'" >> /etc/profile
echo "export https_proxy='http://10.134.99.64:66'" >> /etc/profile

source /etc/profile

#关闭防火墙和selinux

setenforce 0
sed -i "s/enforcing/disabled/g" /etc/selinux/config

systemctl stop firewalld
systemctl disable firewalld

#添加公网DNS
echo "nameserver 8.8.8.8" >> /etc/resolv.conf
echo "nameserver 114.114.114.114" >> /etc/resolv.conf

#时间同步服务
yum –y install chrony
systemctl start chronyd && systemctl enable chronyd
timedatectl set-timezone Asia/Shanghai && timedatectl set-ntp yes
#更新源替换。
yum -y install wget
sleep 6
cd /etc/yum.repos.d/
wget https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/centos/docker-ce.repo

sed -i "s#docker.com#mirrors.tuna.tsinghua.edu.cn/docker-ce#" docker-ce.repo

yum clean all 
yum makecache >/dev/null 2>&1

yum install docker-ce

systemctl start docker
sleep 30
# 判断是否安装成功
flag=$(systemctl is-active docker)
if [[ "$flag" == "active"  ]]
then 
    echo "installed docker"
else
    echo "inactive,please check"
    exit 1

fi

##########
echo "scp daemon.json ,please input master pass"
#编辑daemon.json ,配置docker加速
mkdir /etc/docker
scp root@10.134.196.21:/etc/docker/daemon.json /etc/docker/daemon.json


##########
#编辑docker专用代理
mkdir -p /etc/systemd/system/docker.service.d
echo '[Service]' >/etc/systemd/system/docker.service.d/https-proxy.conf
echo 'Environment="HTTP_PROXY=http://10.134.99.64:66"' >> /etc/systemd/system/docker.service.d/https-proxy.conf

#重新加载配置文件
echo "sighup for docker"
systemctl daemon-reload
systemctl restart docker



















