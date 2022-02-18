from gevent._semaphore import Semaphore  # 使用协程设定集合点、
from locust import events  # 监听事件

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()

def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()  # 创建钩子方法


# events.on_hatch_complete += on_hatch_complete
events.spawning_complete.add_listener(on_hatch_complete)  # 挂载到locust钩子函数（所有的Locust实例产生完成时触发）


all_locusts_spawned.wait()
