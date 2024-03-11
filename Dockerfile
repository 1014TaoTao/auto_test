# 1.基于jenkins/jenkins:latest镜像
FROM jenkins/jenkins:latest

# 2.镜像维护者的姓名和邮箱地址
MAINTAINER zt <948080782@qq.com>


# 3.指定当前工作目录
WORKDIR /var/jenkins_home

#EXPOSE 映射端口
EXPOSE  8080
EXPOSE  50000

# 4.切换到root用户
USER root
RUN sed -i 's#http://deb.debian.org#https://mirrors.aliyun.com#g' /etc/apt/sources.list
# 配置apt-get源
# RUN echo "">sources.list
# RUN echo "deb http://ftp2.cn.debian.org/debian/ buster main">>sources.list
# RUN echo "deb http://ftp2.cn.debian.org/debian/debian-security buster/updates main">>sources.list
# RUN echo "deb http://ftp2.cn.debian.org/debian/debian buster-updates main">>sources.list

RUN cd /var/jenkins_home

# 设定镜像当前时间，否则发送得钉钉消息执行得时候获取到得时间不准备。设置完成可以用date命令查看当前时间
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 1.centos获取最新的软件包
#yum update

# 2.提前安装，以便接下来的配置操作
#yum -y install gcc automake autoconf libtool make
#yum -y install make*
#yum -y install zlib*
#yum install openssl-devel -y //
#yum -y install sudo

# 获取最新的debain软件包
RUN apt-get update
# 升级已安装的软件包
RUN apt-get upgrade
# 提前安装，以便接下来的配置操作
RUN apt-get -y install wget
#RUN apt-get -y install --assume-yes apt-utils
RUN apt-get -y install gcc automake autoconf libtool make
# RUN apt-get -y install make*
RUN apt-get -y install zlib*
RUN apt-get -y install openssl libssl-dev
RUN apt-get -y install sudo
# RUN apt-get install vim

# 5.将当前目录文件夹下的所有文件拷贝到指定目录
# 5.1安装python
RUN apt -y install python3
RUN apt -y install python3-pip
RUN apt -y install python3-venv

# 6.添加软连接
RUN ln -s /usr/local/bin/python3
RUN ln -s /var/jenkins_home/py3.8/bin/pip3/usr/bin/pip3


RUN pip3 instaill pqi
RUN pqi use douban

RUN touch requirements.txt

# 下载allure
RUN wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.17.3/allure-commandline-2.17.3.tgz
RUN tar -zxvf allure-commandline-2.17.3.tgz
RUN mv allure-2.17.3 allure
RUN chmod -R 777 allure

## 配置 allure (记得一行一个回车哦，不然就直接复制粘贴)
#RUN cat >> /root/.bashrc << "EOF"
#RUN export PATH=/var/jenkins_home/allure/bin:$PATH
#RUN EOF

#配置环境变量
ENV PATH=/usr/local/bin/:$PATH
ENV PATH=/var/jenkins_home/allure/bin:$PATH

# 更新环境变量配置文件
RUN source /root/.bashrc

#容器启动时需要执行的命令
RUN java --version
RUN python3 --version
RUN pip --version
RUN allure --version


ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
