# coding:utf8
import queue
import time


from locust import task, TaskSet, events, HttpUser,FastHttpUser  # SequentialTaskSet有序执行、TaskSet无序执行
from locust.runners import MasterRunner

from common import setting
from performance.performance_tool.config import params
from tools.public_tool_log import logger

"""
Locust脚本开发（关联、参数化、检查点、集合点）
"""

logger = logger(setting.PRF_LOG_PATH)



# 开始监听
@events.test_start.add_listener
def on_test_start(environment):
    if not isinstance(environment.runner, MasterRunner):
        logger.info("开始测试设置")
    else:
        logger.info("从主节点开始测试")


# 结束监听
@events.test_stop.add_listener
def on_test_stop(environment):
    if not isinstance(environment.runner, MasterRunner):
        logger.info("清理测试数据")
    else:
        logger.info("从主节点停止测试")


class WebsiteTask(TaskSet):
    index = 0

    # 限制在所有用户准备完成前处于等待状态

    def on_start(self):
        """
        每个user启动前调用on_start方法
        这是获取用户特定测试数据的好地方。每个用户执行一次
        如果不希望记录请求，可以将self.client.<method>替换为request请求
        """
        # 执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time
        # 每个任务执行之后的等待时间
        pass

    def on_stop(self):
        """
        每个user运行结束后调用on_start方法
        清理测试数据等：
        （1）调用接口清理测试数据、（2）数据库清理测试数据
        """
        time.sleep(1)

        # tasks = {test_login1: 3, test_login2: 1}  # 任务权重的第二种选择：执行1的概率是2的3倍
        # tasks = [test_login1, test_login2]  # 任务权重的第三种选择：随机执行列表里面的任务

    @task  # 执行脚本时，只会运行被task标记的方法作为一个测试点，其他方法都是辅助任务的
    def query_pipeline(self):
          # 限制在所有用户准备完成前处于等待状态，集合点
        try:
            datas = self.user.user_data_queue.get() # 随机数据datas
            case_name = 'pipeline列表页查询'
            method = 'GET'
            url = '/kube/v1/api/tekton/pipeline'
            data = {
                "pageNo": 1,
                "pageSize": 10,
                "name": datas['search']
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
                "Content-Type": "application/json;charset=UTF-8",
                "Authorization": params['author']
            }

            logger.info(f"【测试接口名称：{case_name}】===============>> 【start】")
            logger.info(f"【接口类型: {method}】")
            logger.info(f"【接口路径: {params['host']}{url}】")
            logger.info(f"【接口数据: {data}】")
            logger.info(f"【请求头: {headers}】")

            base_url = params['host'] + url
            # 发请求

            with self.client.request(method=method, url=base_url, data=data, headers=headers,
                                     catch_response=True) as response:
                logger.info(f"【响应内容{response.json()}】")
                if response.json()['msg'] == '成功':
                    response.success()
                    logger.info(f"【断言【msg-预期-'成功'】==>【successed】】")
                else:
                    response.failure("Got wrong response")
                    logger.error(f"【断言【msg 预期 '成功'】==>【failed】,原因：{response.json()['msg']}。】")
                logger.info(f"【测试接口名称：{case_name}】===============>> 【end】\n")

        except queue.Empty:
            logger.info(f"【测试数据已用完，结束！】")
            exit(0)

    # @task(20)  # 执行脚本时，只会运行被task标记的方法作为一个测试点，其他方法都是辅助任务的
    # def query_tast(self):
    #     # all_locusts_spawned.wait()  # 限制在所有用户准备完成前处于等待状态
    #     try:
    #         datas = self.user.user_data_queue.get()
    #         case_name = 'task列表页查询'
    #         method = 'GET'
    #         url = '/kube/v1/api/tekton/task/list'
    #         data = {
    #             "pageNo": 1,
    #             "pageSize": 10,
    #             "name": datas['search']
    #         }
    #         headers = {
    #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    #             "Content-Type": "application/json;charset=UTF-8",
    #             "Authorization": params['author']
    #         }
    #         logger.info(f"【测试接口名称：{case_name}】===============>> 【start】")
    #         logger.info(f"【接口类型: {method}】")
    #         logger.info(f"【接口路径: {params['host']}{url}】")
    #         logger.info(f"【接口数据: {data}】")
    #         logger.info(f"【请求头: {headers}】")
    #
    #         base_url = params['host'] + url
    #         # 发请求
    #
    #         with self.client.request(method=method, url=base_url, data=data, headers=headers,
    #                                  catch_response=True) as response:
    #             logger.info(f"【响应内容{response.json()}】")
    #             if response.json()['msg'] == '成功':
    #                 response.success()
    #                 logger.info(f"【断言【msg-预期-'成功'】==>【successed】】")
    #             else:
    #                 response.failure("断言失败")
    #                 logger.error(f"【断言【msg 预期 '成功'】==>【failed】,原因：{response.json()['msg']}。】")
    #             logger.info(f"【测试接口名称：{case_name}】===============>> 【end】\n")
    #
    #
    #     except queue.Empty:
    #         logger.info(f"【测试数据已用完，结束！】")
    #         exit(0)


class WebsiteUser(HttpUser):
    # host = params['host']
    tasks = [WebsiteTask]

    # 循环加入队列
    user_data_queue = queue.Queue()
    for index in range(100):
        datas = {
            "search": "test%03d" % index,
        }
        user_data_queue.put_nowait(datas)
    max_wait = 3000
    min_wait = 1000


if __name__ == '__main__':
    import os

    # os.system(f"locust --config={setting.PRF_CONFIG_PATH}")  # web执行方式
    os.system(f"locust -f locust_demo.py --host={params['host']} --web-host=127.0.0.1 --web-port=8089")  # web执行方式
    # os.system('locust -f locust_demo.py --no-web  -c 1000 -r 100 -n 30000 --run-time 10')# 单位是秒
    # os.system('locust -f locust_demo.py --master --web-host=127.0.0.1')# 单位是秒
    # os.system('locust - f testbaidu.py - -worker - -master - host = 127.0.0.1')  # 此处本地，远程的话使用对应ip即可

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
