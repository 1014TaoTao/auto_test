'''
Author: ZhangTao 948080782@qq.com
Date: 2022-11-30 13:53:50
LastEditors: ZhangTao 948080782@qq.com
LastEditTime: 2022-11-30 14:11:39
FilePath: \pytest_auto_uitest_apitest\tools\common_tools\public_tool_thread.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding: utf-8 -*-

import threading
import time


class PyTimer:
    """定时器类"""

    def __init__(self, func, *args, **kwargs):
        """构造函数"""

        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.running = False

    def _run_func(self):
        """运行定时事件函数"""

        th = threading.Thread(
            target=self.func, args=self.args, kwargs=self.kwargs)
        th.setDaemon(True)
        th.start()

    def _start(self, interval: float, once: bool):
        """启动定时器的线程函数"""

        if interval < 0.010:
            interval = 0.010

        if interval < 0.050:
            dt = interval / 10
        else:
            dt = 0.005

        if once:
            deadline = time.time() + interval
            while time.time() < deadline:
                time.sleep(dt)

            # 定时时间到，调用定时事件函数
            self._run_func()
        else:
            self.running = True
            deadline = time.time() + interval
            while self.running:
                while time.time() < deadline:
                    time.sleep(dt)

                # 更新下一次定时时间
                deadline += interval

                # 定时时间到，调用定时事件函数
                if self.running:
                    self._run_func()

    def start(self, interval: float, once: bool = False):
        """启动定时器

        interval    - 定时间隔，浮点型，以秒为单位，最高精度10毫秒
        once        - 是否仅启动一次，默认是连续的
        """

        th = threading.Thread(target=self._start, args=(interval, once))
        th.setDaemon(True)
        th.start()

    def stop(self):
        """停止定时器"""

        self.running = False


def do_something(name, gender='male'):
    print(time.time(), '定时时间到，执行特定任务')
    print('name:%s, gender:%s' % (name, gender))
    time.sleep(5)
    print(time.time(), '完成特定任务')


timer = PyTimer(do_something, 'Alice', gender='female')
timer.start(0.5, once=False)

input('按回车键结束\n')  # 此处阻塞住进程
timer.stop()
