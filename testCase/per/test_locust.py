# -*- coding: utf-8 -*-

import queue
import logging
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from gevent import monkey
from gevent._semaphore import Semaphore
from locust import HttpUser, TaskSet, task, events, between
from locust.runners import MasterRunner


from tools.yaml_tool import YamlPack

monkey.patch_all()  # 开启协程

# 禁用安全请求警告
# 加上这行代码即可，关闭安全请求警告
urllib3.disable_warnings(InsecureRequestWarning)

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()


def on_hatch_complete(**kwargs):
    """
    Select_task类的钩子方法
    :param kwargs:
    :return:
    """
    all_locusts_spawned.release()


events.spawning_complete.add_listener(on_hatch_complete)


# 开始监听
@events.test_start.add_listener
def on_test_start(environment):
    if not isinstance(environment.runner, MasterRunner):
        logging.info("开始测试设置")
    else:
        logging.info("从主节点开始测试")


# 结束监听
@events.test_stop.add_listener
def on_test_stop(environment):
    if not isinstance(environment.runner, MasterRunner):
        logging.info("清理测试数据")
    else:
        logging.info("从主节点停止测试")


n = 0


class UserBehavior(TaskSet):

    def login(self):
        global n
        n += 1
        print("%s个虚拟用户开始启动，并登录" % n)

    def logout(self):
        print("退出登录")

    def on_start(self):
        self.login()

        all_locusts_spawned.wait()

    def on_stop(self):
        self.logout()

    @task(4)
    def test1(self):
        try:

            # 发请求
            with self.client.request(
                method=method, 
                url=url, 
                data=data, 
                headers=headers,
                catch_response=True
            ) as response:
                logging.info(f"【响应内容{response.json()}】")
                if response.json()['msg'] == msg:
                    response.success()
                    logging.info(f"【断言【msg 预期 {msg}】==>【successes】】")
                else:
                    response.failure("Got wrong response")
                    logging.error(f"【断言【msg 预期 {msg}】==>【fail】,原因：{response.json()['msg']}。】")
                logging.info(f"【测试接口名称：{case_name}】===============>> 【end】\n")

        except queue.Empty:
            logging.info(f"【测试数据已用完...结束！】")
            exit(0)

    @task(6)
    def test2(self):
        try:

            # 发请求
            with self.client.request(method=method, url=url, data=data, headers=headers,
                                     catch_response=True) as response:
                logging.info(f"【响应内容{response.json()}】")
                if response.json()['msg'] == msg:
                    response.success()
                    logging.info(f"【断言【msg 预期 {msg}】==>【successes】】")
                else:
                    response.failure("Got wrong response")
                    logging.error(f"【断言【msg 预期 {msg}】==>【fail】,原因：{response.json()['msg']}。】")
                logging.info(f"【测试接口名称：{case_name}】===============>> 【end】\n")

        except queue.Empty:
            logging.info(f"【测试数据已用完，结束！】")
            exit(0)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]

    wait_time = between(2, 3)  # 直接把等待时间范围使用wait_time写在了自定义方法UserBehavior里


if __name__ == '__main__':
    import os

    api_host = '10.0.34.13:20007'

    os.system(f"locust -f test_locust_demo.py --host={api_host} --web-host=127.0.0.1 --web-port=8089"
              f"--web-port=8089")

    # os.system(f"locust -f {locust_file_path} --host={Config().host_43_13} --web-host=127.0.0.1 --web-port=8089")  # web执行方式
    # os.system(f"locust -f demo.py --no-web -c 30 -r 2 -t 10s --csv=example")  # no-web模式
    # os.system(f"locust --config={setting.PER_CONFIG_PATH}")
    # os.system(f"locust --config={setting.PRF_CONFIG_PATH}")  # web执行方式
    # os.system('locust -f test_locust_demo.py --no-web  -c 1000 -r 100 -n 30000 --run-time 10')# 单位是秒
    # os.system('locust -f test_locust_demo.py --master --web-host=127.0.0.1')# 单位是秒
    # os.system('locust - f testbaidu.py - -worker - -master - host = 127.0.0.1')  # 此处本地，远程的话使用对应ip即可

    # -c 指定运行的最大用户数，对应图形界面中的 Number of total users to simulate
    # -r 指定每秒生成用户数，对应图形界面中的 Hatch rate
    # -t 指定总共运行时长，因在无图形界面中，没有停止按钮，需要有这个参数才能到时间就停止，不然会一直运行下去，直到终端ctrl+c强行停止
    # --host 指定被测服务器域名或ip端口地址
    # --csv 指定输出结果到csv文件的前缀

    '''
            参考结果
                1.Type：请求类型；
                2.Name：请求路径；
                3.requests：当前请求的数量；
                4.fails：当前请求失败的数量；
                5.Median：中间值，单位毫秒，一般服务器响应时间低于该值，而另一半高于该值；
                6.Average：所有请求的平均响应时间，毫秒；
                7.Min：请求的最小的服务器响应时间，毫秒；
                8.Max：请求的最大服务器响应时间，毫秒；
                9.Content Size：单个请求的大小，单位字节；
                10.reqs/sec：每秒钟请求的个数。相当于tps

                charts：
                    实时统计的rps
                    实时统计平均响应时间
                    实时统计虚拟用户数
        '''
