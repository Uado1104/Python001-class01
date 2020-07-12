# 作业一：
# 背景： 网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，
# 探测目标主机是否开放了指定端口（1-1024），用于改善目标主机的安全状况。
# 要求：编写一个基于多进程或多线程模型的主机扫描器。
# 使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
# 使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
# IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
# 需考虑网络异常、超时等问题，增加必要的异常处理。
# 因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。
# 命令行参数举例如下： 
# pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
# pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json
# 说明：
# 因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
# -n：指定并发数量。
# -f ping：进行 ping 测试
# -f tcp：进行 tcp 端口开放、关闭测试。
# -ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
# -w：扫描结果进行保存。
# 选做：
# 通过参数 [-m proc|thread] 指定扫描器使用多进程或多线程模型。
# 增加 -v 参数打印扫描器运行耗时 (用于优化代码)。
# 扫描结果显示在终端，并使用 json 格式保存至文件。
import json
import logging
import logging.handlers
import os
import time

class Logger(object):
  def __init__(self, enable_output_to_file):
    sl_formatter = logging.Formatter('%(asctime)s%(message)s')
    sl_handler = logging.StreamHandler()
    sl_handler.setFormatter(sl_formatter)

    sl_logger = logging.getLogger('stream_logger')
    sl_logger.setLevel(logging.INFO)
    sl_logger.addHandler(sl_handler)

    if enable_output_to_file:
      fl_formatter = logging.Formatter('%(message)s')
      if not os.path.isdir('./logs'):
        os.mkdir('./logs')
      fl_handler = logging.handlers.RotatingFileHandler('logs/log.json', maxBytes=20)
      fl_handler.setFormatter(fl_formatter)

      fl_logger = logging.getLogger('file_logger')
      fl_logger.setLevel(logging.INFO)
      fl_logger.addHandler(fl_handler)

      self.fl_logger = fl_logger

    self.sl_logger = sl_logger

  def log(self, ip, port, result, elapsed):
    msg = f'ip={ip}'
    if port != 0:
      msg = f' {msg} port={port}'
    msg = f' {msg} result={result}'
    if elapsed >= 0:
      msg = f' {msg} elapsed={elapsed}'
    self.sl_logger.info(msg)

    if self.fl_logger is not None:
      d = {'time': time.time(), 'ip': ip}
      if port != 0:
        d['port'] = port
      if elapsed >= 0:
        d['elapsed'] = elapsed

      self.fl_logger.info(json.dumps(d))

