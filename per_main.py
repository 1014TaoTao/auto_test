'''
Author: xxx xx@qq.com
Date: 2022-11-30 13:53:20
LastEditors: xxx xx@qq.com
LastEditTime: 2022-11-30 14:18:49
FilePath: \pytest_auto_uitest_apitest\per_main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# coding: utf-8
from common import setting

if __name__ == '__main__':
    import os

    from common.readConfigIni import Config

    print('wen打开地址: 127.0.0.1:8089')

    os.system(f"locust --config={setting.PER_CONFIG_PATH}")

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
