# Auto_Test

## 项目简介

Auto_Test 是一个完全开源免费的自动化测试框架，旨在整合多种工具和技术，提供全面的API和UI自动化测试解决方案。通过使用Python、pytest、Selenium、pytest-html、requests、openpyxl、pandas、DingTalk、email、Faker、Jenkins等技术，本项目能够帮助开发者高效地进行自动化测试，并生成详细的测试报告。支持通过Jenkins构建发送测试结果通知到邮件和钉钉，方便团队成员及时了解测试状态。

## 关键特性

- **多技术整合**：结合Python、pytest、Selenium等多种工具，实现API和UI自动化测试。
- **详细报告**：使用pytest-html生成美观且详细的测试报告。
- **数据处理**：利用openpyxl和pandas处理Excel数据，方便测试数据管理和结果分析。
- **通知集成**：通过DingTalk发送测试结果通知，确保团队及时了解测试状态。
- **数据伪造**：借助Faker生成假数据，丰富测试场景。
- **持续集成**：通过Jenkins实现持续集成，确保项目代码始终处于良好状态。

## 项目结构

```plaintext
AUTO_TEST
├── basepage           # UI自动化基础类封装目录 
│   └── pages          # UI页面封装目录
├── case               # 测试数据目录
│   ├── api            # 接口测试数据目录
│   └── ui             # UI测试数据目录
├── common             # 全局公共模块
├── config             # 配置文件
├── logs               # 日志目录
├── report             # 测试报告
├── testCase           # 测试用例目录
│   ├── api            # 接口测试用例目录
│   └── ui             # UI测试用例目录
├── tools              # 工具类目录
├── Dockerfile         # Dockerfile文件
├── main.py            # 测试主入口
├── pytest.ini         # pytest配置文件
├── README.md          # 项目说明文档
└── requirements.txt   # 依赖包版本文件
```

## 快速开始

1.工具：

- python下载地址: <https://www.python.org/download>
- pycharm下载地址: <https://www.jetbrains.com/pycharm>

2.搭建步骤

- 2.1拉取代码
  - git clone <https://gitee.com/tao__tao/auto_test.git>
  - 查看本地和远程所有分支： git branch -a
  - 切换分支：git checkout [branch-name]

- 2.2创建虚拟环境：
  - python -m venv venv
  - venv/Scripts/activate
  - 回车激活环境

- 2.3安装项目依赖包
  - pip install -r requirements.txt

- 2.4运行项目
  - 运行前检查config目录中Config.ini文件是否配置正确
  - python main.py

## 参与和支持

如果你觉得这个项目对你有帮助，请给我们一个Star，感谢你的支持!

## 🎨 微信群

在下方为群二维码，可以用于技术交流，也可以一起讨论在项目使用过程中遇到的各种问题。真心希望大家一起优化该项目，积极讨论，让我们一起抱团取暖！

### 群二维码

<table>
    <tr>
      <td><img src="https://gitee.com/tao__tao/fastapi_vue3_admin/raw/master/mkdocs/docs/resources/images/微信.jpg"/></td>
      <td><img src="https://gitee.com/tao__tao/fastapi_vue3_admin/raw/master/mkdocs/docs/resources/images/微信群.jpg"/></td>
      <td><img src="https://gitee.com/tao__tao/fastapi_vue3_admin/raw/master/mkdocs/docs/resources/images/wechatPay.jpg"/></td>
    </tr>
</table>