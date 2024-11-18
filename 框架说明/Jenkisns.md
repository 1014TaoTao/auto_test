# 启动dockerfile

docker build -t zt-jenkins:1.0 ./Dockerfile

# 启动jenkinsfile

docker run -itd -p 10086:8080 -p 50000:50000 -p 10087:44055 -v /home/jenkins/:/var/jenkins_home --name zt-jenkins --restart always --privileged=true -u root jenkins

# -p 9090:8080 jenkins的web访问端口9090

# -v /home/jenkins:/var/jenkins_home 容器/var/jenkins_home路径映射到宿主机/home/jenkins

进入 jenkins 容器 CLI 界面
docker exec -it -uroot jenkins_name bash

安装一些依赖包

# 配置apt-get源

echo "">sources.list
echo "deb <http://ftp2.cn.debian.org/debian/> buster main">>sources.list
echo "deb <http://ftp2.cn.debian.org/debian/debian-security> buster/updates main">>sources.list
echo "deb <http://ftp2.cn.debian.org/debian/debian> buster-updates main">>sources.list
解决linux更新apt软件源时报出GPG错误

# 获取最新的软件包

apt-get update

# 升级已安装的软件包

apt-get upgrade

# 提前安装，以便接下来的配置操作

apt-get -y install gcc automake autoconf libtool make
apt-get -y install make*
apt-get -y install zlib*
apt-get -y install openssl libssl-dev
apt-get install sudo
安装 Python 环境

# 两种方式

# 1 直接使用apt-get安装，此方式安装完成后环境变量已配置

apt-get install python3.6
apt-get install python3-pip

# 2 下载Python安装包，编译安装

cd /usr/local/src
wget <https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz>
tar -zxvf Python-3.6.8.tgz
mv Python-3.6.8 py3.6
cd py3.6

# 编译

./configure --prefix=/var/jenkins_home/py3.6
make && make install

# 添加软连接

ln -s /usr/local/src/py3.6/bin/python3.6 /usr/bin/python3
ln -s /usr/local/src/py3.6/bin/pip3 /usr/bin/pip3

# 更改pip源

mkdir ~/.pip
vi ~/.pip/pipconf
　　　　[global]
　　　　index-url = <https://pypi.tuna.tsinghua.edu.cn/simple>

安装 Allure 环境

# 官网下载 allure 包

# <https://github.com/allure-framework/allure2/releases>

# 先将包上传到主机，然后从主机复制到容器内

docker cp allure-commandline-2.13.6.tgz jenkins1:/usr/local/src

# 解压

<!-- unzip allure-commandline-2.13.6.zip -->
tar -zxvf allure-commandline-2.13.6.tgz

# 赋予文件夹所有内容最高权限

mv allure-2.13.6 allure
chmod -R 777 allure

# 配置 allure 和 py 环境变量（逐行输入）

cat >> /root/.bashrc << "EOF"
export PATH=/usr/local/src/allure/bin:$PATH
export PATH=/usr/local/src/py3.6/bin:$PATH
EOF

# jenkins安装好后，页面配置

全局工具配置
    jdk:
        通过export查看jdk环境变量，并写入jenkins
        别名：JAVA_HOME
        路径：/opt/java/openjdk

    git:
        通过which is git查导git路径
        别名：git
        路径：/usr/bin/git

    allure:
        jenkins全局配置allure
        别名：allure
        路径：/usr/local/src/allure
        环境变量：
            SystemVersion:Windows10-64bit
            PythonVersion:python-3.8.10
            AllureVersion:allure-2.16.1
            ProjectName:pytest_auto_uitest_apitest
            Author:xxx
            Email:xx@qq.com

系统配置：
