@ECHO OFF
CHCP 65001
ECHO.::::::::::::::请保持窗口开启或最小化，测试结束前请勿关闭:::::::::::::::

ECHO.:: 					                             ::

ECHO.::                            接口测试                               ::

ECHO.:: 					                             ::

ECHO.::                          作者： 张 涛                             ::

ECHO.:: 					                             ::

ECHO.::                           版本  V1.0.0                            ::

ECHO.:: 					                             ::

ECHO.::                          时间 2018.11.10                          ::

ECHO.:: 					                             ::

ECHO :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

ECHO.[ INFO ] 运行环境准备

REM 从配置文件中安装环境依赖库
if exist requirements.txt pip install -r requirements.txt
if not exist requirements.txt echo requirements.txt does not exist

REM 运行脚本
python main.py
pause >nul