<!--
 * @Author: ZhangTao 948080782@qq.com
 * @Date: 2022-11-30 13:53:20
 * @LastEditors: ZhangTao 948080782@qq.com
 * @LastEditTime: 2022-11-30 14:19:05
 * @FilePath: \pytest_auto_uitest_apitest\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

# 项目名称：pytest_auto_unitest_apitest

## 一、项目及框架的搭建

1.工具：

- python 下载地址: <https://www.python.org/download>

- pycharm 下载地址: <https://www.jetbrains.com/pycharm>

- jdk 下载地址: <https://repo.huaweicloud.com/java/jdk/>

- allure(需要安装 jdK)下载地址: <https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/>

  2.搭建步骤

- 2.1 拉取代码

  - git clone <http://gitlab.e-tudou.com/tudou-autotest-project/pytest_auto_uitest_apitest.git>

  - 查看本地和远程所有分支 git branch -a

  - 切换分支 git checkout [branch-name]

- 2.2 创建虚拟环境：

  - python -m venv venv

  - venv/Scripts/activate

  - 回车激活虚拟环境

- 2.3pip 更换源：

  - pip install pqi 安装一次就够了

  - pqi ls

  - pqi use aliyun 更换阿里云源

- 2.4 安装项目依赖包

  - pip install -r requirements.txt

## 二.工程目录

```text.
pytest_auto_uitest_apitest:   # 项目父目录
├─auto_shell    # 工作中涉及的脚本文件（方便工作中使用）
├─basepage    # ui自动化基础类封装目录
├─bat    # bat文件目录，存放bat脚本
├─case    # 测试用例存放目录
│  ├─api    # 接口测试用例目录
│  ├─prf    # 性能测试用例目录
│  └─ui   # UI测试用例目录
├─common    # 全局公共模块
├─config     # 全局配置文件
├─data     # 测试数据依赖文件路径
├─driver    # ui自动化浏览器驱动存放目录
├─logs    # 日志存放目录
├─pages   # ui自动化存放page所有功能封装类
├─report    # 测试报告
├─testCase    # 测试用例脚本入口目录
│  ├─api    # 接口测试脚本入口
│  ├─per    # 性能测试脚本入口
│  └─ui   # UI测试脚本入口
├─tools   # 项目依赖工具类封装
├─venv    # 项目虚拟环境
├─api_main.py   # 接口测试入口
├─per_main.py   # 性能测试入口
├─ui_main.py    # UI测试入口
├─pytest.ini    # 全局测试框架配置文件
├─Dockerfile    # docker打包脚本
├─Jenkinsfile   # jenkins构建脚本
├─locust.conf   # 性能测试配置文件
├─README.md   # 项目说明文档
├─备份信息   # 项目相关备份文件（用于复制）
├─框架文件   # 项目readme.md文件依赖照片
└─框架说明    # 项目使用说明书
```

## 三.项目说明

> ./框架说明/API_README.md # 接口自动化说明 \

    ./框架说明/Per_README.md     # 性能自动化说明 \
    ./框架说明/UI_README.md      # UI自动化说明
