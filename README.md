# 项目名称：pytest_auto_unitest_apitest

## 一、项目及框架的搭建:

1.工具：

  - python下载地址: https://www.python.org/download

  - pycharm下载地址: https://www.jetbrains.com/pycharm

  - jdk下载地址: https://repo.huaweicloud.com/java/jdk/

  - allure(需要安装jdK)下载地址: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

2.搭建步骤

- 2.1拉取代码
  
  - git clone http://gitlab.e-tudou.com/tudou-autotest-project/pytest_auto_uitest_apitest.git
  
  - 查看本地和远程所有分支 git branch -a
  
  - 切换分支 git checkout [branch-name]

- 2.2创建虚拟环境：

  - python -m venv venv

  -  venv/Scripts/activate

  -  回车激活虚拟环境

- 2.3pip更换源：
  
  -  pip install pqi 安装一次就够了
  
  -  pqi ls
    
  -  pqi use aliyun 更换阿里云源

- 2.4安装项目依赖包

  - pip install -r requirements.txt


## 二.工程目录： 

```text.
pytest_auto_uitest_apitest:   # 项目父目录
├─auto_shell    # 工作中涉及的脚本文件（方便工作中使用）
│  ├─assa   # saas相关的脚本
│  ├─kube   # kube相关的脚本
│  ├─middleDataCenter   # 中台相关的脚本
│  └─添加授权 # kube授权相关的脚本
├─basepage    # ui自动化基础类封装目录 
├─bat    # bat文件目录，存放bat脚本
├─case    # 测试用例存放目录
│  ├─api    # 接口测试用例目录
│  │  ├─excel_data    # excel样式测试用例（已excel为后续主要扩展方向）
│  │  ├─sql_data    # sql相关测试用例
│  │  └─yaml_data   # yaml格式的测试用例
│  ├─prf    # 性能测试用例目录
│  │  └─yaml_data   # yaml格式的测试用例
│  └─ui   # UI测试用例目录
│      ├─excel_data   # excel样式测试用例（已excel为后续主要扩展方向）
│      ├─sql_data   # sql相关测试用例
│      └─yaml_data    # yaml格式的测试用例
├─common    # 全局公共模块
├─config     # 全局配置文件
├─data     # 测试数据依赖文件路径
├─driver    # ui自动化浏览器驱动存放目录
├─logs    # 日志存放目录
│  ├─api_logs   # 接口日志
│  ├─prf_logs   # 性能日志
│  └─ui_logs    # ui日志
├─pages   # ui自动化存放page所有功能封装类
├─report    # 测试报告
│  ├─api_report   # 接口测试报告
│  ├─per_report   # 性能测试报告
│  └─ui_report    # UI测试报告
├─static    # pyqt设计相关模板文件（与整个框架无关）
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

>   ./框架说明/API_README.md     # 接口自动化说明 \
    ./框架说明/Per_README.md     # 性能自动化说明 \
    ./框架说明/UI_READNE.md      # UI自动化说明

  