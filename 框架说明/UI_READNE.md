## allure常用装饰器
    ## allure.dynamic 动态属性
    @allure.dynamic.severity
    @allure.dynamic.feature
    @allure.dynamic.link
    @allure.dynamic.issue
    @allure.dynamic.testcase
    @allure.dynamic.story
    @allure.dynamic.title('动态标题')
    @allure.dynamic.description('动态描述')
    1）功能模块方面的特性：
    
        1）feature（主要功能模块--一级标签）
            使用方法：@allure.feature()
        2）story（子功能模块--二级标签）
            使用方法：@allure.story()
    
    2）测试用例方面的特性：
        
        1）title（测试用例标题）
            使用方法： @allure.title
        2）description（测试用例描述）
            使用方法：@allure.description()
        3）step（测试用例步骤）
            使用方法：@allure.step()
    
    3）测试用例级别的特性：severity（BUG严重级别）
     
        1）使用方法：@allure.severity(allure.severity_level.CRITICAL)或者 @allure.severity('critical')
    
        2）相关说明：　Allure中对严重级别的定义：
            blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
            critical级别：临界缺陷（ 功能点缺失）
            normal级别：普通缺陷（数值计算错误）
            minor级别：次要缺陷（界面错误与UI需求不符）
            trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
    
    4）：链接方面的特性： 
        
        link/issue/testcase（链接）
        使用方法：
        @allure.link(url='http://www.baidu.com',name='link_url')
        @allure.issue(url='http://www.baidu.com',name='issue_url') #bug链接
        @allure.testcase(url='http://www.tapd.com',name='testcase_url')
    
    
    5）：附件信息方面的特性： 
    
        attach（附件信息）
        使用方法：@allure.attach(body, name, attachment_type, extension)
        
        body - 要写入文件的原始内容
        name - 包含文件名的字符串
        attachment_type - 其中一个allure.attachment_type值
        extension - 提供的将用作创建文件的扩展名


```python
url = "https://www.baidu.com/"
text = "天天向上"
BaiduPage01().open_baidu(url, "跳转百度页面")
screen("跳转百度页面")
BaiduPage01().query_baidu(text, "搜索好好学习")
screen("搜索好好学习")

with allure.step('步骤1：打开网页'):
    BaiduPage01().open_baidu(url,"跳转百度页面")
    screen("跳转百度页面")
    allure.attach('{}'.format(url), name='网页地址')
with allure.step('步骤2：开始搜索'):

    BaiduPage01().query_baidu(text,"搜索好好学习")
    allure.attach('{}'.format(text), name='搜索内容')
    screen("搜索好好学习")
```

pytest学习系列_pytest-timeout插件之设置超时时间
pip install pytest-timeout

更改默认命令行选项，当我们用命令行运行时，需要输入多个参数，很不方便。比如想测试完生成报告，失败重跑两次，一共运行两次，通过分布式去测试，如果在命令行中执行的话，命令会很长，很不方便
-s -v -q --alluredir ./report/allure_result --rerun=2 --count=2  -n=auto



[pytest]
addopts = -s -v -q --alluredir ./report/allure_result --rerun=2 --count=2  -n=auto
testpaths = ./testCase/
python_files = test_*.py   test_*.py  *_test .py  test*.py
python_classes = Test*   Test_*  test*  test_*
python_functions = test_*  test*
minversion = 6.2.5
log_cli = 1
log_cli_level = DEBUG
log_cli_date_format = %Y-%m-%d-%H-%M-%S
log_cli_format = %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s
log_file = test.log
timeout = 30



basepage ——selenium的基类，对selenium的方法进行封装
pageelements——页面元素，把页面元素单独提取出来，放入一个文件中
searchpage ——页面对象类，把selenium方法和页面元素进行整合
testcase ——使用pytest对整合的searchpage进行测试用例编写


-o report/allure-report：allure报告生成的位置【指定目录生成测试报告】
-c report/allure-report：新的allure报告生成之前先把先前的allure报告清理掉
