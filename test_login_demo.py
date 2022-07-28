# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# File       : test_two.py
# Time       ：2021/11/22 20:36
# Author     ：tzs
# version    ：python 3.6
# Description：
'''
import json
import multiprocessing
from threading import Thread

import pytest
from common.utils import *
from common.excel_util import *


data = r'C:\Users\Administrator\.jenkins\workspace\psimsendemail\untitled\data\login_data.xlsx'
data_res = r'C:\Users\Administrator\.jenkins\workspace\psimsendemail\untitled\report\test_report.xlsx'

def test_login():
    ws = load_workbook(data)
    ws.save(data_res)
    for i in range(0,100):
        if (excel[i]['是否执行']) != 'Y':
            ExcelHandler.write(data_res,'app',i+2,11,'此版本不测试')
        else:
            url = excel[i]['请求URL']  # 接口URL
            method = excel[i]['请求方法']  #请求方法
            d = eval(excel[i]['请求参数'])  #获取传入接口的参数
            r = request(url=url,method=method,data=d)
            print(r.text)
            try:
                assert int(excel[i]['状态码']) == r.json()['msg_code']  #断言响应码
                assert excel[i]['返回信息'] == r.json()['msg']  #断言响应信息
                ExcelHandler.write(data_res,'app',i+2,11,'PASS')
            except Exception as e:
                ExcelHandler.write(data_res,'app',i+2,11,'fail')

# def test1():
#     _processes = []
#     for index in range(1):
#         # _process = multiprocessing.Process(target=TestLogin().test_login())
#         _process = Thread(target=test_login)
#         _process.start()
#         _processes.append(_process)
#     for _process in _processes:
#         _process.join()
'''
pytest-parallel 支持python3.6及以上版本，所以如果想做多进程并发在linux或者mac上做，在Windows上不起作用（Workers=1），
如果做多线程linux/mac/windows平台都支持，进程数为workers的值
pytest test.py --workers 3 ：3个进程运行
pytest test.py --tests-per-worker 4 ：4个线程运行
pytest test.py --workers 2 --tests-per-worker 4 ：2个进程并行，且每个进程最多4个线程运行，即总共最多8个线程运行。
'''

if __name__ == '__main__':
    pytest.main(["-vs", "-n", '4'])
