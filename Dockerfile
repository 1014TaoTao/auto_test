FROM python:3.8.2


LABEL author="zhangtao"
LABEL email="948080782@qq.com"
LABEL desc="dockerfile for xtest"

COPY . /www

WORKDIR /www

RUN pip install -r requirements.txt

WORKDIR /www/public

EXPOSE 5000

ENTRYPOINT ["python","api_main.py"]