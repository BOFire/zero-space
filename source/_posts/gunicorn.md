title: gunicorn
author: 沐汐
tags:
  - python部署
  - ''
categories:
  - 程序小记
date: 2021-08-20 09:53:00
---
### 总线
	Nginx => Gunicorn => Flask/Django
    
### Gunicorn 介绍

	gunicorn是一个python Wsgi http server，只支持在类Unix系统上运行，来源于Ruby的unicorn项目。Gunicorn使用prefork master-worker模型（在gunicorn中，master被称为arbiter），能够与各种wsgi web框架协作。
    
### 安装
	pip3 install gunicorn
  
### 配置
	项目路径：gunicorn.conf
#### 配置内容
	server socket

    bind
    监听地址和端口。

    backlog
    服务器中在pending状态的最大连接数，即client处于waiting的数目。超过这个数目， client连接会得到一个error。
    建议值64-2048。

    worker 进程

    workers
    worker进程的数量。建议值2-4 x $(NUM_CORES)， 缺省为1。

    worker_class
    worker进程的工作方式。 有 sync, eventlet, gevent, tornado, gthread, 缺省值sync。

    threads
    工作进程中线程的数量。建议值2-4 x $(NUM_CORES)， 缺省值1。
    此配置只适用于gthread 进程工作方式， 因为gevent这种使用的是协程工作方式。

    worker_connections
    客户端最大同时连接数。只适用于eventlet， gevent工作方式。

    max_requests
    worker重启之前处理的最大requests数， 缺省值为0表示自动重启disabled。主要是防止内存泄露。

    max_requests_jitter
    抖动参数，防止worker全部同时重启。

    timeout
    通常设为30。

    graceful_timeout
    接收到restart信号后，worker可以在graceful_timeout时间内，继续处理完当前requests。

    keepalive
    server端保持连接时间。

    security

    limit_request_line
    http request line最大字节数。值范围0-8190， 0表示无限制。

    limit_request_field
    http request中 header字段数的最大值。缺省为100，最大32768。

    limit_request_field_size
    http request header字段最大字节数。0表示无限制。

    调试

    reload
    当代码有修改时，自动重启workers。适用于开发环境。

    reload_extra_files
    扩展reload配置，增加templates，configurations等文件修改监控。

    spew
    跟踪程序执行的每一行。

    check_config
    检查配置。

    server 机制

    sendfile
    系统底层拷贝数据方式，提供performance。

    chdir
    在app加载之前，进入到此目录。

    daemon
    应用是否以daemon方式运行。

    raw_env
    key=value, 传递环境参数。

    pidfile
    pid存储文件路径。

    worker_tmp_dir
    临时工作目录。

    user
    指定worker进程的运行用户名。

    group
    指定worker进程运行用户所在组。

    umask
    gunicorn创建文件的缺省权限。

    pythonpath
    附加到python path的目录列表。

    日志

    accesslog
    访问日志文件路径。

    access_log_format
    日志格式。 例如 %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" 。

    errorlog
    错误日志路径。

    loglever
    日志级别。debug, info, warning, error, critical.

    capture_output
    重定向stdout/stderr到error log file。

    logger_class
    日志实现类。缺省gunicorn.glogging.Logger 。

    logconfig
    日志配置文件。同python标准日志模块logging的配置。

    进程名

    proc_name
    设置进程名(setproctitle)，在ps，top等命令中会看到. 缺省值为default_proc_name配置。
    server钩子

    on_starting
    on_reload
    when_ready
    pre_fork
    post_fork
    post_worker_init
    worker_init
    worker_abort
    pre_exec
    pre_request
    post_request
    child_exit
    worker-exit
    nworkers_changed
    on_exit
    

    
### 运行
#### 指令运行
	gunicorn gunicorn_demo:app
#### 配置运行
	gunicorn 工程名字.wsgi -c gunicorn配置文件夹/配置文件要改
    
### 备注

+ 如果用到异步的worker模型，需要安装对应的模块（如gevent）
+ 搭配supervisor进程管理
