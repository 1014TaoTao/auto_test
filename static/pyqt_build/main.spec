# -*- mode: python ; coding: utf-8 -*-

import sys
import os.path as osp
sys.setrecursionlimit(6000)


block_cipher = None

SETUP_DIR = 'E:\\pytest_auto_uitest_apitest\\'

py_files = [
    'E:\\pytest_auto_uitest_apitest\\main.py',
    'E:\\pytest_auto_uitest_apitest\\common\\consts.py',
    'E:\\pytest_auto_uitest_apitest\\common\\readConfigYaml.py',
    'E:\\pytest_auto_uitest_apitest\\common\\setting.py',
    'E:\\pytest_auto_uitest_apitest\\testCase\\conftest.py',
    'E:\\pytest_auto_uitest_apitest\\testCase\\test_excel.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\allure_tools\\public_tool_allurereport.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\assert_tools\\api_tool_assert.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\common_tools\\api_tool_global_var.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\common_tools\\api_tool_headers.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\common_tools\\api_tool_login.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\common_tools\\api_tool_open_html.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\common_tools\\public_tool_localip.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\common_tools\\public_tool_manager.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\common_tools\\public_tool_run_all.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\email_tools\\public_tool_email.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\excel_tools\\api_tool_excel.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\excel_tools\\api_tool_read_excel.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\excel_tools\\public_tool_openpyxl.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\logs_tools\\public_tool_log.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\requests_tools\\api_tool_reponse.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\requests_tools\\api_tool_request.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\send_news_tools\\public_tool_dingding.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\system_tools\\public_tool_project_check.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\time_tools\\public_tool_time.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\txt_tools\\api_tool_read_pyqt_txt.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\yaml_tools\\api_tool_yaml.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\zip_tools\\public_tool_zip.py',
    'E:\\pytest_auto_uitest_apitest\\tools\\pyqt_toos\\api_tool_run.py'
]

# 自己的依赖 ‘所在文件夹目录‘，’文件夹名‘
add_files = [
    (SETUP_DIR+'logs', 'logs'),
    (SETUP_DIR+'case', 'case'),
    (SETUP_DIR+'images', 'images'),
    (SETUP_DIR+'data', 'data'),
    (SETUP_DIR+'config', 'config'),
#    (SETUP_DIR+'common', 'common'),
#    (SETUP_DIR+'tools', 'tools'),
    (SETUP_DIR+'testCase', 'testCase'),
    (SETUP_DIR+'report', 'report'),
#    (SETUP_DIR+'备份信息','备份信息'),
#    (SETUP_DIR+'框架文件','框架文件'),
#    (SETUP_DIR+'pytest.ini','.'),
#    (SETUP_DIR+'README.md','.'),
#    (SETUP_DIR+'requirements.txt','.')
]

#配置文件等其他例如python中调用的dll，exe等 ’dll或exe文件名‘，’.‘
files = [
#    (SETUP_DIR+'logs', 'logs'),
#    (SETUP_DIR+'case', 'case'),
#    (SETUP_DIR+'images', 'images'),
#    (SETUP_DIR+'data', 'data'),
#    (SETUP_DIR+'config', 'config'),
#    (SETUP_DIR+'common', 'common'),
#    (SETUP_DIR+'tools', 'tools'),
#    (SETUP_DIR+'testCase', 'testCase'),
#    (SETUP_DIR+'report', 'report'),
#    (SETUP_DIR+'备份信息','备份信息'),
#    (SETUP_DIR+'框架文件','框架文件'),
    (SETUP_DIR+'pytest.ini','.'),
#    (SETUP_DIR+'README.md','.'),
#    (SETUP_DIR+'requirements.txt','.')
]

#第三方依赖
package = [
#    'allure-pytest',
#    'allure-python-commons',
#    'anyio',
#    'async-generator',
#    'atomicwrites',
#    'attrs',
#    'Brotli',
#    'certifi',
#    'cffi',
#    'chardet',
#    'charset-normalizer',
#    'click',
#    'colorama',
#    'colorlog',
#    'ConfigArgParse',
#    'cryptography',
#    'DingtalkChatbot',
#    'docopt',
#    'et-xmlfile',
#    'Faker',
#    'filetype',
#    'Flask',
#    'Flask-BasicAuth',
#    'Flask-Cors',
#    'future',
#    'gevent',
#    'geventhttpclient',
#    'greenlet',
#    'h11',
#    'httpcore',
#    'httpx',
#    'idna',
#    'importlib-metadata',
#    'iniconfig',
#    'itsdangerous',
#    'Jinja2',
#    'jsonpath',
#    'locust',
#    'loguru',
#    'MarkupSafe',
#    'msgpack',
#    'openpyxl',
#    'outcome',
#    'packaging',
#    'pluggy',
#    'psutil',
#    'py',
#    'pycparser',
#    'pymongo',
#    'PyMySQL',
#    'pyOpenSSL',
#    'pyparsing',
#    'PyQt5',
#    'PyQt5-Qt5',
#    'PyQt5-sip',
#    'PyQt5-stubs',
#    'pytest',
#    'python-dateutil',
#    'pytz',
#    'pywin32',
#    'PyYAML',
#    'pyzmq',
#    'requests',
#    'rfc3986',
#    'roundrobin',
#    'selenium',
#    'six',
#    'sniffio',
#    'sortedcontainers',
#    'toml',
#    'trio',
#    'trio-websocket',
#    'typing_extensions',
#    'urllib3',
#    'Werkzeug',
#    'win32-setctime',
#    'wsproto',
#    'xlrd',
#    'xlutils',
#    'xlwt',
#    'zipp',
#    'zope.event',
#    'zope.interface'
]

a = Analysis(
    py_files,
    pathex=['D:\\python\\Python37\\libs','D:\\python\\Python37\\Lib\\site-packages'],
#    binaries=[],
    binaries=files,
    datas=add_files,
    hiddenimports=package,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
#    console=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='E:\\apiTestTool\\icon\\Sun.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
