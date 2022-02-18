# 性能自动化

    locust架构上使用master-slave模型，支持单机和分布式
    master和slave（即worker）使用 ZeroMQ 协议通讯
    提供web页面管理master，从而控制slave，同时展示压测过程和汇总结果
    可选no-web模式（headless 一般用于调试）
    基于Python本身已经支持跨平台
   2. Locust安装方式
   同样，我们直接 pip安装即可

    2.1 安装 locust
    pip install  locust
    2.2 安装pyzmq
    如果打算运行Locust 分布在多个进程/进程，需要安装pyzmq
    同样使用pip安装
    
    -h, --help    查看帮助
    -H HOST, --host=HOST    指定被测试的主机，采用以格式：http://10.21.32.33
    --web-host=WEB_HOST    指定运行 Locust Web 页面的主机，默认为空 ''。
    -P PORT, --port=PORT, --web-port=PORT    指定 --web-host 的端口，默认是8089
    -f LOCUSTFILE, --locustfile=LOCUSTFILE    指定运行 Locust 性能测试文件，默认为: locustfile.py
    --csv=CSVFILEBASE, --csv-base-name=CSVFILEBASE    以CSV格式存储当前请求测试数据。
    --master    Locust 分布式模式使用，当前节点为 master 节点。
    --slave    Locust 分布式模式使用，当前节点为 slave 节点。
    --master-host=MASTER_HOST    分布式模式运行，设置 master 节点的主机或 IP 地址，只在与 --slave 节点一起运行时使用，默认为：127.0.0.1.
    --master-port=MASTER_PORT    分布式模式运行， 设置 master 节点的端口号，只在与 --slave 节点一起运行时使用，默认为：5557。注意，slave 节点也将连接到这个端口+1 上的 master 节点。
    --master-bind-host=MASTER_BIND_HOST    Interfaces (hostname, ip) that locust master should bind to. Only used when running with --master. Defaults to * (all available interfaces).
    --master-bind-port=MASTER_BIND_PORT    Port that locust master should bind to. Only used when running with --master. Defaults to 5557. Note that Locust will also use this port + 1, so by default the master node will bind to 5557 and 5558.
    --expect-slaves=EXPECT_SLAVES    How many slaves master should expect to connect before starting the test (only when --no-web used).
    --no-web    no-web 模式运行测试，需要 -c 和 -r 配合使用.
    -c NUM_CLIENTS, --clients=NUM_CLIENTS    指定并发用户数，作用于 --no-web 模式。
    -r HATCH_RATE, --hatch-rate=HATCH_RATE    指定每秒启动的用户数，作用于 --no-web 模式。
    -t RUN_TIME, --run-time=RUN_TIME    设置运行时间, 例如： (300s, 20m, 3h, 1h30m). 作用于 --no-web 模式。
    -L LOGLEVEL, --loglevel=LOGLEVEL    选择 log 级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）. 默认是 INFO.
    --logfile=LOGFILE    日志文件路径。如果没有设置，日志将去 stdout/stderr
    --print-stats    在控制台中打印数据
    --only-summary    只打印摘要统计
    --no-reset-stats    Do not reset statistics once hatching has been completed。
    -l, --list    显示测试类, 配置 -f 参数使用
    --show-task-ratio    打印 locust 测试类的任务执行比例，配合 -f 参数使用.
    --show-task-ratio-json    以 json 格式打印 locust 测试类的任务执行比例，配合 -f 参数使用.
    -V, --version    查看当前 Locust 工具的版本.


####Locust的代码分为以下模块：

    User-压测用例：提供了HttpUser压测http协议，用户可以定义事务，断言等，也可以实现特定协议的User
    Runner-执行器：Locust的核心类，定义了整个框架的执行逻辑，实现了Master、Slave（worker）等执行器
    EventHook-事件钩子：通过预先定义的事件使得我们可以在这些事件发生时(比如slave上报)做一些额外的操作
    WebU：提供web界面的操作台和压测过程展示
    Socket-通信器：提供了分布式模式下master和slave的交互方式
    RequestStats-采集、分析器：定义了结果分析和数据上报格式

    Locust主要由下面的几个库构成：

1) gevent

gevent是一种基于协程的Python网络库，它用到Greenlet提供的，封装了libevent事件循环的高层同步API。

2) flask

Python编写的轻量级Web应用框架。

3) requests

Python Http库

4) msgpack-python

MessagePack是一种快速、紧凑的二进制序列化格式，适用于类似JSON的数据格式。msgpack-python主要提供MessagePack数据序列化及反序列化的方法。

5) six

Python2和3兼容库，用来封装Python2和Python3之间的差异性

6) pyzmq

pyzmq是zeromq(一种通信队列)的Python绑定,主要用来实现Locust的分布式模式运行

####核心类

    用户定义的User类作为Runner的user_classes传入
    TaskSet和User持有client，可以在类中直接发起客户端请求，client可以自己实现，Locust只实现了HttpUser
    master的client_listener监听施压端client消息
    slave的worker方法监听master消息
    slave的stats_reporter方法上报压测数据，默认3s上报一次
    slave的start启动协程，使用master分配的并发数开始压测
    slave默认1s上报一次心跳，如果master超过3s未收到某个slave的心跳则会将其标记为missing状态
    主要结构介绍完了，接下来看下具体的类和对应的方法

    用户行为User task TaskSet
    一个User代表一个压测用户。locust将为每个正在模拟的用户生成User类的一个实例。
    【User可定义公共属性】
    
    2.1.1. wait_time属性：单位秒，两次执行task时间的间隔。between、constant、constant_pacing
    eg：自定义wait_time下面的User类将休眠一秒钟，然后休眠两个，然后休眠三个，依此类推
    
    2.1.2. weight属性：通过设置weight参数，设置用户比例
    eg：网络用户的可能性是移动用户的三倍
    
    2.3 TaskSet
    用于模拟现实用户分级操作的场景，单接口直接用User就可以。
    TaskSet是蝗虫任务的集合，将像直接在User类上声明的任务一样执行，使用户在两次任务执行之间处于休眠状态.


| 工具简单对比 | LoadRunner | Jmeter |Locust |
| :----| :----: | :----: |:----: |
| 压力生成器 | √ | √ | √ |
| 负载控制器 | √ | √ | √ |
| 系统资源监控器 | √ | x | x |
| 结果采集器 | √ | √ | √ |
| 结果分析器 | √ | √ | √ |
| 授权方式 | 商业收费 | 开源 | 开源 |
| 开发语言 | C/Java | Java | python |
| 测试脚本形式 | C/Java | GUI | python |
| 并发机制 | 线程/进程 | 线程 | 协程（gevent） |
| 单机并发能力 | 低 | 低 | 高 |
| 分布式压力 | 支持 | 支持 | 支持 |
| 资源监控 | 支持 | 不支持 | 不支持 |
| 报告与分析 | 完善 | 简单图表 | 简单图表 |
| 支持二次开发 | 不支持 | 支持 | 支持 |

.Locust 与Jmeter占用资源比较
Locust之所以在资源占用方面完胜开源的Jmeter，
主要是因为：
>>两者的模式用户方式不同：
①Jmeter是通过线程来作为虚拟用户
②Locust借助gevent库对协程的支持，以greenlet来实现对用户的模拟你。
所以，在相同配置下，Locust能支持的并发用户数相比Jmeter，就不止提升了一个Level。
2、并发机制
①Locust的并发机制采用协程（gevent）的机制。
②采用多线程来模拟多用户时，线程数会随着并发数的增加而增加，而线程之间的切换是需要占用资源的，IO的阻塞和线程的sleep会不可避免的导致并发效率下降；正因如此，LoadRunner和Jmeter这类采用进程和线程的测试工具，都很难在单机上模拟出较高的并发压力。
③而协程和线程的区别在于：协程避免了系统级资源调度，由此大幅提高了性能。
④正常情况下，单台普通配置的测试机可以生产数千并发压力，这是LoadRunner和Jmeter都无法实现的。


Runner状态机
在分布式场景下，除了数据一致性，状态同步也是非常重要的。在Locust的master-slave架构下，需要管理master和slave的状态，不仅为了控制压测的开始或停止，也是为了掌握当前的压力机情况。那么都有哪些状态？

| 状态 | 说明 |
| :----| :---- |
| ready| 准备就绪，master和slave启动后默认状态 |
| hatching| 正在孵化压力机，对master来说正在告诉slave们开始干活，对slave来说是过渡状态，因为它们马上要running |
| running| 正在压测 |
| cleanup| 当发生GreenletExit时的状态，一般不会出现 |
| stopping| 表示正在通知slave们停止，只有master有这个状态 |
| stopped| 压测已经停止 |
| missing| 状态丢失，只有slave有的状态，默认3秒如果master没有收到slave的心跳就会认为它missing了，一般是进程没有正常退出导致 |

 ![image](https://img-blog.csdnimg.cn/img_convert/deaff4d83740f421f52c133cc15d39ba.png)
 ![image](https://img-blog.csdnimg.cn/20200624135911307.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1eW91ZGV5dWVy,size_16,color_FFFFFF,t_70)


四、相关术语
1.负载：
模拟业务操作对服务器造成压力的过程，比如2000个用户进行下单操作。
2.性能测试(Performance Testing)：
模拟用户负载来测试系统在负载情况下，系统的响应时间，吞吐量等指标是否满足性能要求。
3.负载测试(Load Testing)
在一定软硬件环境下，通过不断加大负载(不同虚拟用户数)来确定在满足性能指标情况下能够承受的最大用户数。
>>这里性能指标包含：TPS(每秒事务数)，RT(事务平均响应时间)，CPU Using(CPU使用率)，Mem Using(内存使用情况)等软硬件指标。
4.配置测试(Configuration Testing)
为了合理的调配资源，提高系统运行效率，通过测试手段来获取，验证，调整配置信息的过程。
5.压力/强度测试(Stress Testing)
在一定软硬件环境下，通过高负载的手段来使服务器的资源(强调的是服务器资源，硬件资源)处于一个极限状态，测试系统在极限状态下长时间运行是否稳定。
>>确定稳定的指标，包含：TPS(每秒事务数)，RT(事务平均响应时间)，CPU Using(CPU使用率)，Mem Using(内存使用情况)等。
6.稳定测试(Endurance Testing)
在一定软硬件环境下，长时间运行一定负载，确定系统在满足性能指标的前提下是否运行稳定。这里强调一下，稳定性测试并不是在极限状态下来运行的，这与上面第五条的压力/强度测试 是不一样的。
一般我们会在满足性能要求的负载情况下加大到1.5 ~ 2倍的负载量进行测试。
7.TPS
每秒完成的事务数，通常指每秒成功的事务数，性能测试中重要的综合性能指标。一个事务是一个业务度量单位。
举个例子：
比如支付操作，在后台系统可能会经历会员系统，财务系统，支付系统，会计系统，银行网关等，但是针对用户来说，我就想知道我从下单到付款成功共花费多长时间。
8.RT/ART(Response Time/average Response Time)
响应时间/平均响应时间，指一个事务花费多长时间完成。我们更多的时候，是统计很多次响应时间，然后去平均值，这样保证了时间的准确性，同时也更具代表性。
>>通常，我们写RT，来代替ART。
9.PV(Page View)
每秒用户访问页面的次数。
>>此参数是用来分析平均每秒有多少用户来访问页面
10.Vuser(Virtual user)
虚拟用户数。即模拟真实业务逻辑步骤的虚拟用户，虚拟用户模拟的操作步骤都被记录在虚拟用户脚本里。Vuser脚本用户描述Vuser在场景中执行的操作。
11.并发：
并发最主要要有两点：点层面上和线层面上。
①点层面上的：
例如：周一早上7:30半，小学生要统一到操场升国旗。
>>即：同一时间做某件事
②线层面上的：
例如：中午11:30-13:00，小学生有的跳皮筋，有的踢足球，但同时对服务器产生压力。
>>即：一个时间段做不同的事
这里不做过多介绍，详细可以看小鱼写的这篇《常见并发问题》，里面有对并发的详细解读。
12.场景(Scenario)
性能测试过程中为了模拟真实用户的业务处理过程，在LR中构建的基于事务、脚本、虚拟用户、运行设置、运行计划、监控、分析等一系类动作的集合，称之为性能测试场景。
>>场景中包含：待执行的脚本、脚本组、并发数、负载生成器、测试目标、测试执行时的配置条件等。
13.思考时间(Think Time)
模拟真实用户在实际操作过程中停顿的时间间隔。
>>从业务角度来讲：思考时间是用户在操作时，每个请求之间的时间间隔；
>>从测试脚本来讲：是两个请求语句之间的时间间隔。
14.标准差(Std. Deviation)
根据数据统计的概念得来，标准差越小，说明波动越小，系统越稳定，反之，则说明系统不稳定。
>>包含：响应时间标准差，TPS标准差，Running Vuser标准差，Load标准差，CPU Using标准差等等。

五、性能工具
市面上的性能测试工具，还蛮多的，但是我们熟知，且使用最多的 JMeter 和Loadrunner这两款，那么，我们要怎么选性能测试工具、市面上又有哪些性能测试工具呢？
1.如何选择性能测试工具
我们在选择工具的时候，无非从以下几个方面来考虑：
①专业，稳定，高效。
②简单易上手，在测试脚本上不需要花费太多时间。
③有技术支持，文档健全。
④投入与产出比。
2.常见性能工具有哪些
①HP公司的 Loadrunner
②Apache JMeter
③Grinder
④CompuWare 公司的QALoad
⑤Microsoft 公司的WAS
⑥RadView公司的WebLoad
⑦IBM公司的RPT
⑧OPENSTA等
在这里，小鱼强调一下，性能测试的核心不是选择什么工具，而是性能分析，重要的是思想，实现方式，这与选择什么工具，并无太大关系，
所以一定要分析主次。

六、通过标准
判断性能测试是否通过，不仅是看TPS，RT，而是要从服务端性能，前端性能，和用户体验性能来分析。
常见的测试通过标准如下：
![image](https://img-blog.csdnimg.cn/20200625003829690.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3d1eW91ZGV5dWVy,size_16,color_FFFFFF,t_70)


    locustfile = ./locust_demo.py
    host = http://10.0.34.13:10007
    users = 50 #并发 Locust 用户的峰值数量。主要与–headless 或–autostart 一起使用。可以在测试期间通过键盘输入 w、W（生成 1、10 个用户）和 s、S（停止 1、10 个用户）来更改
    # spawn-rate = 10 # 以（每秒用户数）生成用户的速率。主要与 –headless 或 –autostart 一起使用
    hatch-rate = 5 ==抑制==
    # headful = # ==抑制==
    # headless = true # 禁用 Web 界面，并立即开始测试。使用 -u 和 -t 控制用户数和运行时间
    # expect-workers = 0 # expect-workers 在开始测试之前，master 应该期望连接多少个worker（仅当使用–headless/autostart 时）。
    # expect-workers-max-wai = 5s# 主人在放弃之前应该等待工人连接多长时间。默认为永远等待
    web-host = "127.0.0.1/" # 将 Web 界面绑定到的主机。默认为“*”（所有接口）
    web-port = "8089" #运行 Web 主机的端口
    # # web-auth = # 为 Web 界面打开基本身份验证。应按以下格式提供：用户名：密码
    # autostart = true  # 立即开始测试（不禁用 Web UI）。使用 -u 和 -t 控制用户数和运行时间
    # autoquit = 3s # 在运行完成 X 秒后完全退出 Locust。仅与 –autostart 一起使用。默认设置是保持 Locust 运行，直到您使用 CTRL+C 将其关闭
    # # tags =# 要包含在测试中的标签列表，因此只有具有任何匹配标签的任务才会被执行
    # # exclude-tags =# 要从测试中排除的标签列表，因此只会执行没有匹配标签的任务
    # csv = result_csv  # 以 CSV 格式将当前请求统计信息存储到文件中。设置此选项将生成三个文件：[CSV_PREFIX]_stats.csv、[CSV_PREFIX]_stats_history.csv 和 [CSV_PREFIX]_failures.csv
    # csv-full-history = result_history# 将每个统计信息条目以 CSV 格式存储到 _stats_history.csv 文件中。您还必须指定“–csv”参数才能启用此功能。
    # html = result_html # 存储 HTML 报告文件
    # # print-stats =# 在控制台中打印统计信息
    # # only-summary =# 仅打印摘要统计信息
    # skip-log-setup = false # 禁用 Locust 的日志记录设置。相反，配置由 Locust 测试或 Python 默认值提供。
    # loglevel = INFO # 在调试/信息/警告/错误/关键之间进行选择。默认为信息。
    # logfile = logs # 日志文件的路径。如果未设置，日志将转到 stderr
    run-time = 15s # 在指定的时间后停止，例如（300s、20m、3h、1h30m 等）。仅与 –headless 或 –autostart 一起使用。默认永远运行。
    
    # worker = # 设置 locust 以分布式模式运行，此进程作为 worker
    # master = true # 设置 locust 以分布式模式运行，此进程作为主进程
    # master-bind-host = # locust master 应该绑定的接口（主机名、ip）。仅在使用 –master 运行时使用。默认为 *（所有可用接口）。
    # master-bind-port = # locust master 应该绑定的端口。仅在使用 –master 运行时使用。默认为 5557。
    # master-host = # 用于分布式负载测试的 locust master 的主机或 IP 地址。仅在使用 –worker 运行时使用。默认为 127.0.0.1。
    # master-port  = # locust master 使用要连接的端口进行分布式负载测试。仅在使用 –worker 运行时使用。默认为 5557。
    # reset-stats =# 产卵完成后重置统计信息。在分布式模式下运行时，应在 master 和 worker 上都设置
    # exit-code-on-error =# 设置当测试结果包含任何失败或错误时使用的进程退出代码
    # stop-timeout =# 在退出之前等待模拟用户完成任何正在执行的任务的秒数。默认是立即终止。该参数只需要在运行 Locust 分布式时为主进程指定。
    
    # tls-cert = # 用于通过 HTTPS 提供服务的 TLS 证书的可选路径
    # tls-key =# 用于通过 HTTPS 提供服务的 TLS 私钥的可选路径
    
    
    loglevel = INFO
    logfile = locustfile.log
    autostart = true
    csv = result_csv
    csv-full-history = true
    html = true
