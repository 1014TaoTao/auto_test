# ����dockerfile
docker build -t zt-jenkins:1.0 ./Dockerfile
# ����jenkinsfile
docker run -itd -p 10086:8080 -p 50000:50000 -p 10087:44055 -v /home/jenkins/:/var/jenkins_home --name zt-jenkins --restart always --privileged=true -u root jenkins

Jenkins ��װ
docker run -itd -p 10086:8080 -p 50000:50000 -p 10087:44055 -v /home/jenkins/:/var/jenkins_home --name zt-jenkins --restart always --privileged=true -u root jenkins

# -p 9090:8080 jenkins��web���ʶ˿�9090

# -v /home/jenkins:/var/jenkins_home ����/var/jenkins_home·��ӳ�䵽������/home/jenkins

���� jenkins ���� CLI ����
docker exec -it -uroot jenkins_name bash
 
��װһЩ������
# ����apt-getԴ
echo "">sources.list
echo "deb http://ftp2.cn.debian.org/debian/ buster main">>sources.list
echo "deb http://ftp2.cn.debian.org/debian/debian-security buster/updates main">>sources.list
echo "deb http://ftp2.cn.debian.org/debian/debian buster-updates main">>sources.list
���linux����apt���Դʱ����GPG����

# ��ȡ���µ������
apt-get update

# �����Ѱ�װ�������
apt-get upgrade

# ��ǰ��װ���Ա�����������ò���
apt-get -y install gcc automake autoconf libtool make
apt-get -y install make*
apt-get -y install zlib*
apt-get -y install openssl libssl-dev
apt-get install sudo
��װ Python ����
# ���ַ�ʽ
# 1 ֱ��ʹ��apt-get��װ���˷�ʽ��װ��ɺ󻷾�����������
apt-get install python3.6
apt-get install python3-pip
# 2 ����Python��װ�������밲װ
cd /usr/local/src
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
tar -zxvf Python-3.6.8.tgz
mv Python-3.6.8 py3.6
cd py3.6

# ����
./configure --prefix=/var/jenkins_home/py3.6
make && make install

# ���������
ln -s /usr/local/src/py3.6/bin/python3.6 /usr/bin/python3
ln -s /usr/local/src/py3.6/bin/pip3 /usr/bin/pip3
# ����pipԴ

mkdir ~/.pip
vi ~/.pip/pipconf
��������[global]
��������index-url = https://pypi.tuna.tsinghua.edu.cn/simple

��װ Allure ����
# �������� allure ��
# https://github.com/allure-framework/allure2/releases

# �Ƚ����ϴ���������Ȼ����������Ƶ�������
docker cp allure-commandline-2.13.6.zip jenkins1:/usr/local/src
# ��ѹ
unzip allure-commandline-2.13.6.zip

# �����ļ��������������Ȩ��
mv allure-2.13.6 allure
chmod -R 777 allure

# ���� allure �� py �����������������룩
cat >> /root/.bashrc << "EOF" 
export PATH=/usr/local/src/allure/bin:$PATH 
export PATH=/usr/local/src/py3.6/bin:$PATH 
EOF