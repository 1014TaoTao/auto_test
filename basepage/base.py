# -*- coding: utf-8 -*-
import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from common import setting
from tools.logi_tool import logger

success = "SUCCESS"
fail = "FAIL   "


class Page:
    """
    页面基础类，用于所有页面的继承
    """

    def __init__(self, driver, parent=None):
        self.driver = driver
        self.timeout = 20
        self.logger = logger(setting.UI_LOG_PATH)
        self.parent = parent
        self.pass_num = 0
        self.fail_num = 0

    # 打开网址
    def open_url(self, url: str):
        """
        打开网址.
        用法:
        driver.open("https://www.fengsulian.com")
        """
        start_time = time.time()
        try:
            self.driver.get(url)
            self.logger.info("{0}==> 打开网址 {1}, 花费 {2} 秒".format(
                success, url, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法加载 {1}, 花费 {2} 秒".format(
                fail, url, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 设置网页地址格式
    def get_nowpage_url(self):
        return self.driver.current_url

    # 失败截图
    def fail_img(self) -> str:
        file_name = 'fail%s.png' % (time.strftime("%Y_%m_%d_%H_%M_%S"))
        file_path = setting.UI_FAIL_IMG_PATH + "\\" + file_name
        if not os.path.exists(setting.UI_FAIL_IMG_PATH):
            os.makedirs(setting.UI_FAIL_IMG_PATH)
        self.driver.get_screenshot_as_file(file_path)
        return file_path

    # 断言截图
    def assert_img(self) -> str:
        file_name = 'assert%s.png' % (time.strftime("%Y_%m_%d_%H_%M_%S"))
        file_path = setting.UI_ASS_IMG_PATH + "\\" + file_name
        if not os.path.exists(setting.UI_ASS_IMG_PATH):
            os.makedirs(setting.UI_ASS_IMG_PATH)
        self.driver.get_screenshot_as_file(file_path)
        return file_path

    # 获取当前窗口截图
    def take_nowpage_screenshot(self) -> str:
        """
        获取当前窗口截图.

        用法:
        driver.take_screenshot('c:/test.png')
        """
        start_time = time.time()
        file_name = '%s.png' % (time.strftime("%Y_%m_%d_%H_%M_%S"))
        file_path = setting.UI_OR_IMG_PATH + "\\" + file_name
        if not os.path.exists(setting.UI_OR_IMG_PATH):
            os.makedirs(setting.UI_OR_IMG_PATH)
        try:
            self.driver.get_screenshot_as_file(file_path)
            self.logger.info("{0}==> 截图当前页并保存,截图路径: {1}, 花费 {2} 秒".format(success,
                                                                          file_path,
                                                                          "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法截图当前页并保存,截图路径: {1}, 花费 {2} 秒".format(fail,
                                                                             file_path,
                                                                             "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise
        return file_path

    # 显性等待或叫动态等待
    def _element_wait(self, css, secs=2):
        """
        显性等待或叫动态等待.

        用法:
        driver._element_wait("id==kw",10)
        """
        # if "==" not in css:
        #     raise NameError("Positioning syntax errors, lack of '=='.")

        # by = css.split("==")[0].strip()
        # value = css.split("==")[1].strip()
        by = css[0].strip()
        messages = '元素: {0} 没有在 {1} 秒内找到，尝试重新调整定位时间.'.format(css, secs)

        if by == "id":
            WebDriverWait(self.driver, secs, 0.5).until(
                ec.presence_of_element_located(css), messages)
        elif by == "name":
            WebDriverWait(self.driver, secs, 0.5).until(
                ec.presence_of_element_located(css), messages)
        elif by == "class name":
            WebDriverWait(self.driver, secs, 0.5).until(
                ec.presence_of_element_located(css), messages)
        elif by == "link text":
            WebDriverWait(self.driver, secs, 0.5).until(
                ec.presence_of_element_located(css), messages)
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 0.5).until(
                ec.presence_of_element_located(css), messages)
        elif by == "css selector":
            WebDriverWait(self.driver, secs, 0.5).until(
                ec.presence_of_element_located(css), messages)
        else:
            raise NameError(
                "请输入正确的定位元素,'id','name','class','link_text','xpath','css'.")

    # 隐性等待
    def implicitly_wait(self, secs):
        """
        隐性等待.

        用法:
        driver.wait(10)
        """
        start_time = time.time()
        self.driver.implicitly_wait(secs)
        self.logger.info("{0}==> 设定隐性等待所有元素 {1} 秒, 花费 {2} 秒".format(success,
                                                                    secs, "%.4f" % (time.time() - start_time)))

    # 强制等待
    def sleep_wait(self, secs):
        """
        强制等待.

        用法:
        sleep(10)
        """
        time.sleep(secs)
        self.logger.info("{0}==> 强制等待 {1} 秒".format(success, secs))

    # 定位元素
    def _get_element(self, css):
        """
        判断元素定位方式，并返回元素.

        用法:
        driver._get_element('id==kw')
        """
        # if "==" not in css:
        #     raise NameError("Positioning syntax errors, lack of '=='.")

        # by = css.split("==")[0].strip()
        # value = css.split("==")[1].strip()
        by = css[0].strip()
        value = css[1].strip()
        if by == "id":
            element = self.driver.find_element(by, value)
        elif by == "name":
            element = self.driver.find_element(by, value)
        elif by == "class name":
            element = self.driver.find_element(by, value)
        elif by == "link text":
            element = self.driver.find_element(by, value)
        elif by == "xpath":
            element = self.driver.find_element(by, value)
        elif by == "css selector":
            element = self.driver.find_element(by, value)
        else:
            raise NameError(
                "请输入正确的定位元素,'id','name','class','link_text','xpath','css'.")
        return element

    # 窗口最大化
    def max_window(self):
        """
        设置浏览器窗口最大化.
        """
        start_time = time.time()
        self.driver.maximize_window()
        self.logger.info("{0}==> 设置窗口最大化, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))

    # 设置网页窗口尺寸
    def set_window(self, wide, high):
        """
        设置浏览器窗口宽高.

        用法:
        driver.set_window(wide,high)
        """
        start_time = time.time()
        self.driver.set_window_size(wide, high)
        self.logger.info("{0}==> 设置窗口尺寸,宽: {1},高: {2}, 花费 {3} 秒".format(success,
                                                                        wide, high,
                                                                        "%.4f" % (time.time() - start_time)))

    # 输出文本
    def text_input(self, css, text):
        """
        操作输入框.

        用法:
        driver.type("id==kw","selenium")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            el = self._get_element(css)
            el.send_keys(text)
            self.logger.info("{0}==> 定位元素: <{1}> 输入内容: {2}, 花费 {3} 秒 ".format(success,
                                                                              css1, text,
                                                                              "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法定位元素: <{1}> 输入内容: {2}, 花费 {3} 秒".format(fail,
                                                                                css1, text,
                                                                                "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 清除和输入元素
    def clear_type(self, css, text):
        """
        清除和输入元素.

        用法:
        driver.clear_type("id==kw","selenium")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            el = self._get_element(css)
            el.clear()
            el.send_keys(text)
            self.logger.info("{0}==> 清空文本定位元素: <{1}> 输入内容: {2}, 花费 {3} 秒".format(success,
                                                                                 css1, text,
                                                                                 "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法定位清空文本元素: <{1}> 输入内容: {2}, 花费 {3} 秒".format(fail,
                                                                                    css1, text,
                                                                                    "%.4f" % (
                                                                                        time.time() - start_time)))
            self.fail_img()
            raise

    # 点击事件
    def click(self, css):
        """
        可以点击任意文字/图片可以点击
         连接、复选框、单选按钮，甚至下拉框等..

        用法:
        driver.click("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]

        try:
            self._element_wait(css)
            el = self._get_element(css)
            el.click()
            self.logger.info("{0}==> 点击元素: <{1}>, 花费 {2} 秒".format(
                success, css1, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法找到点击元素: <{1}>, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 鼠标右击
    def right_click(self, css):
        """
        右键单击元素.

        用法:
        driver.right_click("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            el = self._get_element(css)
            ActionChains(self.driver).context_click(el).perform()
            self.logger.info(
                "{0}==> 鼠标右击定位元素: <{1}>, 花费 {2} 秒".format(success, css1, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法找到鼠标右击定位元素: <{1}>, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 移动
    def move_to_element(self, css):
        """
        将鼠标悬停在元素上.

        用法:
        driver.move_to_element("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            el = self._get_element(css)
            ActionChains(self.driver).move_to_element(el).perform()
            self.logger.info("{0}==> 移动元素: <{1}>, 花费 {2} 秒".format(
                success, css1, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法找到移动元素: <{1}>, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 双击
    def double_click(self, css):
        """
        双击元素.

        用法:
        driver.double_click("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            el = self._get_element(css)
            ActionChains(self.driver).double_click(el).perform()
            self.logger.info("{0}==> 双击元素: <{1}>, 花费 {2} 秒".format(
                success, css1, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法找到双击元素: <{1}>, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img(

            )
            raise

    # 拖动并释放
    def drag_and_drop(self, el_css, ta_css):
        """
        将元素拖动一定距离然后将其放下.

        用法:
        driver.drag_and_drop("id==kw","id==su")
        """
        start_time = time.time()
        try:
            self._element_wait(el_css)
            element = self._get_element(el_css)
            self._element_wait(ta_css)
            target = self._get_element(ta_css)
            ActionChains(self.driver).drag_and_drop(element, target).perform()
            self.logger.info("{0}==> 拖动元素: <{1}> 到元素: <{2}>, 花费 {3} 秒".format(success,
                                                                              el_css, ta_css,
                                                                              "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法找到拖动元素: <{1}> 到元素: <{2}>, 花费 {3} 秒".format(fail,
                                                                                   el_css, ta_css,
                                                                                   "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 点击超链接内容

    def click_text(self, text):
        """
        单击链接文本旁边的元素

        用法:
        driver.click_text("新闻")
        """
        start_time = time.time()
        try:
            # self.driver.find_element_by_partial_link_text(text).click()  # 弃用
            self.driver.find_element(by=By.LINK_TEXT(text)).click()
            self.logger.info("{0}==> 点击超链接内容: {1}, 花费 {2} 秒".format(
                success, text, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法找到可以点击的超链接内容: {1}, 花费 {2} 秒".format(fail, text, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 关闭当前窗口
    def close(self):
        """
        模拟用户单击弹出窗口或选项卡标题栏中的“关闭”按钮.

        用法:
        driver.close()
        """
        start_time = time.time()
        self.driver.close()
        self.logger.info("{0}==> 关闭当前窗口, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))

    # 关闭浏览器
    def quit(self):
        """
        退出浏览器并关闭所有窗口.

        用法:
        driver.quit()
        """
        start_time = time.time()
        self.driver.quit()
        self.logger.info("{0}==> 关闭所有窗口并退出浏览器, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))

    # 提交
    def submit(self, css):
        """
        提交指定表格.

        用法:
        driver.submit("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            el = self._get_element(css)
            el.submit()
            self.logger.info("{0}==> 提交元素: <{1}>, 花费 {2} 秒".format(
                success, css1, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法找到可提交元素: <{1}>, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 刷新网页
    def f5(self):
        """
        刷新当前页面.

        用法:
        driver.F5()
        """
        start_time = time.time()
        self.driver.refresh()
        self.logger.info("{0}==> 刷新网页, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))

    # 执行js脚本,参数为脚本内容，一般为字符串”“
    def js(self, script):
        """
        执行 JavaScript 脚本.

        用法:
        driver.js("window.scrollTo(200,1000);")
        """
        start_time = time.time()
        try:
            self.driver.execute_script(script)
            self.logger.info(
                "{0}==> 执行js脚本: {1}, 花费 {2} 秒".format(success, script, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 该执行js脚本无效: {1}, 花费 {2} 秒".format(fail,
                                                                       script, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # def driver_add_token(self):
    #     from tools.common_tools.api_tool_login import UiLogin
    #     # 获取token
    #     token = UiLogin().ui_login()
    #     print(token)
    #     # 添加token
    #     js = f'window.localStorage.setItem("token", {token})'
    #     self.js(script=js)

    # 获取属性
    def get_attribute(self, css, attribute):
        """
        获取元素属性的值.

        用法:
        driver.get_attribute("id==su","href")
        """
        start_time = time.time()
        try:
            self._element_wait(css)
            el = self._get_element(css)
            attr = el.get_attribute(attribute)
            self.logger.info("{0}==> 获取属性元素: <{1}>,属性为: {2}, 花费 {3} 秒".format(success,
                                                                              css, attribute,
                                                                              "%.4f" % (time.time() - start_time)))
            return attr
        except Exception:
            self.logger.error("{0}==> 无法找到获取属性元素: <{1}>,属性为: {2}, 花费 {3} 秒".format(fail,
                                                                                   css, attribute,
                                                                                   "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 获取元素文本
    def get_text(self, css):
        """
        获取元素文本信息.

        用法:
        driver.get_text("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            text = self._get_element(css).text
            self.logger.info(
                "{0}==> 获取元素文本: <{1}>, 花费 {2} 秒".format(success, css1, "%.4f" % (time.time() - start_time)))
            return text
        except Exception:
            self.logger.error(
                "{0}==> 无法找到获取元素文本元素: <{1}>, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 获取网页标题
    def get_title(self):
        """
        获取窗口标题.

        用法:
        driver.get_title()
        """

        start_time = time.time()
        title = self.driver.title
        self.logger.info("{0}==> 取网页标题, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))
        return title

    # 获取网页地址
    def get_url(self):
        """
        获取当前页面的URL地址.

        用法:
        driver.get_url()
        """
        start_time = time.time()
        url = self.driver.current_url
        self.logger.info("{0}==> 获取网页地址, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))
        return url

    # accept()弹框点击确认
    def accept_alert(self):
        """
        接受警告框.

        用法:
        driver.accept_alert()
        """
        start_time = time.time()
        self.driver.switch_to.alert.accept()
        self.logger.info("{0}==> 弹框点击确认, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))

    # dimiss()弹框点击取消
    def dismiss_alert(self):
        """
        关闭警告框.

        用法:
        driver.dismiss_alert()
        """
        start_time = time.time()
        self.driver.switch_to.alert.dismiss()
        self.logger.info("{0}==> 弹框点击取消, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))

    # 进入窗口所在框架
    def switch_to_frame(self, css):
        """
        切换窗口所在框架

        用法:
        driver.switch_to_frame("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            iframe_el = self._get_element(css)
            self.driver.switch_to.frame(iframe_el)
            self.logger.info(
                "{0}==> 进入窗口所在框架: <{1}>, 花费 {2} 秒".format(success, css1, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法找到进入窗口所在框架元素: <{1}>, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 退出窗口所在框架
    def switch_to_frame_out(self):
        """
        返回下一个更高级别的当前表单机器表单(退出窗口所在框架)。
         与switch_to_frame()方法的对应关系.

        用法:
        driver.switch_to_frame_out()
        """
        start_time = time.time()
        self.driver.switch_to.default_content()
        self.logger.info("{0}==> 退出窗口所在框架, 花费 {1} 秒".format(
            success, "%.4f" % (time.time() - start_time)))

    # 打开新窗口，将鼠标切换到新打开的窗口
    def open_new_window(self, css):
        """
        打开新窗口，将鼠标切换到新打开的窗口。

        用法:
        driver.open_new_window("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            original_windows = self.driver.current_window_handle
            self._element_wait(css)
            el = self._get_element(css)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            self.logger.info("{0}==> 点击元素: <{1}> 打开新的窗口并进入, 花费 {2} 秒".format(success,
                                                                             css1, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法找到点击元素: <{1}> 打开新的窗口并进入, 花费 {2} 秒".format(fail,
                                                                                  css1,
                                                                                  "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 元素已在
    def element_exist(self, css):
        """
        判断元素是否存在，返回结果为真或假.

        用法:
        driver.element_exist("id==kw")
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            self.logger.info(
                "{0}==> 动态等待定位元素: <{1}> 存在, 花费 {2} 秒".format(success, css1, "%.4f" % (time.time() - start_time)))
            return True
        except TimeoutException:
            self.logger.error(
                "{0}==> 动态等待定位元素: <{1}> 不存在, 花费 {2} 秒".format(fail, css1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            return False

    # 切换浏览器窗口
    def into_new_window(self):
        """
        进入新窗口.

        用法:
        dirver.into_new_window()
        """
        start_time = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            self.logger.info("{0}==> 切换浏览器窗口,窗口地址: {1}, 花费 {2} 秒".format(success,
                                                                         self.driver.current_url,
                                                                         "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法切换浏览器窗口, 花费 {1} 秒".format(
                fail, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 定位元素输入文本然后回车（针对点击按钮等无效的情况可以使用）
    def type_and_enter(self, css, text, secs=0.5):
        """
        操作输入框。 1、输入信息，休眠0.5s；2、输入ENTER。.

        用法:
        driver.type_css_keys('id==kw','beck')
        """
        start_time = time.time()
        css1 = css[0] + "==" + css[1]
        try:
            self._element_wait(css)
            ele = self._get_element(css)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            self.logger.info("{0}==> 定位元素 <{1}> 输入内容: {2},等待时间 {3} 秒,点击回车, 花费 {4} 秒".format(
                success, css1, text, secs, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法找到定位元素 <{1}> 输入内容: {2},等待时间 {3} 秒,点击回车, 花费 {4} 秒".
                              format(fail, css1, text, secs, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 通过js定位点击
    def js_click(self, css):
        """
        输入一个 css 选择器，使用 js click 元素。

        用法:
        driver.js_click('#buttonid')
        """
        start_time = time.time()
        js_str = "$('{0}').click()".format(css)
        try:
            self.driver.execute_script(js_str)
            self.logger.info(
                "{0}==> 通过js脚本定位点击，js脚本内容: {1}, 花费 {2} 秒".format(success, js_str, "%.4f" % (time.time() - start_time)))
        except Exception:
            self.logger.error("{0}==> 无法通过js脚本定位点击，js脚本内容: {1}, 花费 {2} 秒".format(fail,
                                                                                 js_str,
                                                                                 "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 滚动条定位坐标（horizontal（水平）,vertical（垂直）），在当前窗口/框架 同步执行javaScript
    def scroll_bar(self, horizontal, vertical):
        """
        控制滚动条
        """
        start_time = time.time()
        js_str = "window.scrollTo({0},{1})".format(horizontal, vertical)
        try:
            self.driver.execute_script(js_str)
            self.logger.info("{0}==> 通过js脚本设定滚动条，js脚本内容，滚动条位置: {1}, 花费 {2} 秒".format(success, js_str,
                                                                                     "%.4f" % (
                                                                                         time.time() - start_time)))
        except Exception:
            self.logger.error(
                "{0}==> 无法通过js脚本设定滚动条，js脚本内容，滚动条位置: {1}, 花费 {2} 秒".format(fail, js_str,
                                                                          "%.4f" % (time.time() - start_time)))
            self.fail_img()
            raise

    # 多元素定位
    def find_elements(self, *loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except Exception:
            self.logger.info("%s 无法找到定位元素 %s 在页面中." % (self, loc))
            raise "%s 无法找到定位元素 %s 在页面中." % (self, loc)

    # 判断指定的元素中是否包含了预期的字符串，返回布尔值(包含关系)
    def is_text_in_element(self, locator, text):
        """
        判断文本在元素里,没定位到元素返回False，定位到返回判断结果布尔值
        用法:
        result = driver.text_in_element(locator, text)
        """
        start_time = time.time()
        locator1 = locator[0] + "==" + locator[1]
        try:
            WebDriverWait(self.driver, self.timeout, 0.5).until(
                ec.text_to_be_present_in_element(locator, text))
            self.logger.info(
                "{0}==> 定位到元素: <{1}> , 花费 {2} 秒".format(success, locator1, "%.4f" % (time.time() - start_time)))
            self.pass_num += 1
            result = "pass"
            return result

        except TimeoutException:
            self.logger.error(
                "{0}==> 元素无法定位: <{1}> , 花费 {2} 秒".format(fail, locator1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            self.fail_num += 1
            result = "fail"
            return result

    # 判断指定元素的属性值中是否包含了预期的字符串，返回布尔值(等于关系)
    def is_text_in_value(self, locator, value):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        用法:
        result = driver.text_in_element(locator, text)
        """
        start_time = time.time()
        locator1 = locator[0] + "==" + locator[1]
        try:
            WebDriverWait(self.driver, self.timeout, 0.5).until(
                ec.text_to_be_present_in_element_value(locator, value))
            self.logger.info("{0}==> 定位到元素: <{1}> , 花费 {2} 秒".format(success,
                                                                     locator1, "%.4f" % (time.time() - start_time)))
            self.pass_num += 1
            result = "pass"
            return result
        except TimeoutException:
            self.logger.error("{0}==> 元素无法定位: <{1}> , 花费 {2} 秒".format(fail,
                                                                       locator1, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            self.fail_num += 1
            result = "fail"
            return result

    # 判断title==title(等于关系)
    def titie_is_value(self, title):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        用法:
        result = driver.text_in_element(locator, text)
        """
        start_time = time.time()

        try:
            WebDriverWait(self.driver, self.timeout, 0.5).until(
                ec.title_is(title))
            self.logger.info("{0}==> 判断网页标题: <{1}> ,实际标题<{2}> 花费 {3} 秒".format(success,
                                                                               title, self.get_title(),
                                                                               "%.4f" % (time.time() - start_time)))
            self.pass_num += 1
            result = "pass"
            return result
        except TimeoutException:
            self.logger.error("{0}==> 判断网页标题: <{1}> ,实际标题<{2}> 花费 {3} 秒".format(fail,
                                                                                title, self.get_title(),
                                                                                "%.4f" % (time.time() - start_time)))
            self.fail_img()
            self.fail_num += 1
            result = "fail"
            return result

    # 判断title包含text(包含关系)
    def value_in_titie(self, text):
        """
        判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        用法:
        result = driver.text_in_element(locator, text)
        """
        start_time = time.time()

        try:
            WebDriverWait(self.driver, self.timeout, 0.5).until(
                ec.title_contains(text))
            self.logger.info("{0}==> 判断网页标题包含: <{1}> , 花费 {2} 秒".format(success,
                                                                        text, "%.4f" % (time.time() - start_time)))
            self.pass_num += 1
            result = "pass"
            return result
        except TimeoutException:
            self.logger.error("{0}==> 判断网页标题包含: <{1}> , 花费 {2} 秒".format(fail,
                                                                         text, "%.4f" % (time.time() - start_time)))
            self.fail_img()
            self.fail_num += 1
            result = "fail"
            return result

    # 断言相等
    def assert_equal(self, loc, text):
        """
        断言

        用法:
        assert(loc==text)
        """
        start_time = time.time()
        try:
            assert (loc == text)
            self.logger.info("{0}==> 断言: {1} == {2}, 花费 {3} 秒".format(success, loc,
                                                                      text, "%.4f" % (time.time() - start_time)))
            self.pass_num += 1
            result = "pass"
            return result
        except Exception:
            self.logger.error("{0}==> 断言: {1} != {2}, 花费 {3} 秒".format(fail, loc,
                                                                       text, "%.4f" % (time.time() - start_time)))
            self.assert_img()
            self.fail_num += 1
            result = "fail"
            return result

    # 断言不相等
    def assert_notequal(self, loc, text):
        """
        断言

        用法:
        assert(loc！=text)
        """
        start_time = time.time()
        try:
            assert (loc != text)
            self.logger.info("{0}==> 断言: {1} != {2}, 花费 {3} 秒".format(success, loc,
                                                                      text, "%.4f" % (time.time() - start_time)))
            self.pass_num += 1
            result = "pass"
            return result
        except Exception:
            self.logger.error("{0}==> 断言: {1} == {2}, 花费 {3} 秒".format(fail, loc,
                                                                       text, "%.4f" % (time.time() - start_time)))
            self.assert_img()
            self.fail_num += 1
            result = "fail"
            return result

    # 将目标属性处理为空
    def js_clear_text(self, css):
        """
        将目标属性处理为空

        """
        js_str = None
        css1 = css[0].capitalize()
        css2 = css[1]
        css3 = css[0] + "==" + css[1]
        start_time = time.time()
        try:
            js_str = "document.getElementBy{0}({1}).target=' ';".format(
                css1, css2)
            self.driver.execute_script(js_str)
        except Exception:
            self.logger.info("{0}==> 定位属性，<{1}> ,js脚本: {2}，花费 {3} 秒".format(success,
                                                                            css3, js_str,
                                                                            "%.4f" % (time.time() - start_time)))
            raise "无法定位到元素，导致不能将目标属性处理为空"

# if __name__ == '__main__':
#     from basepage.browser import select_browser
#     p = Page(select_browser)
#     p.driver_add_token()
#     p.select_browser()
#     p.open_url(url="https://www.baidu.com/")
#     p.max_window()
#     p.implicitly_wait(30)
#     css = ("id", "kw")
#     text = "天天向上"
#     p.type_and_enter(css, text)
