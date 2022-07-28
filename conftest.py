# coding:utf-8

import pytest
import requests
import sys
sys.dont_write_bytecode = True
from selenium import webdriver
'''向session传入token进行调用'''
@pytest.fixture(scope='session')
def get_token(url,params=None,data=None,json=None,**kwargs):
    s = requests.session()     #构造⼀个全局session对象，这里就包含了登录成功后的cookie
    res = s.post(url, params=params, data=data, json=json, **kwargs).text
    try:
        res = json.loads(res)
        token = res["token"]
        return token
    except ValueError:
        print("not json")

@pytest.fixture(scope='session')
def action():
    print("测试用例开始".center(30, '*'))
    yield
    print("测试用例结束".center(30, '*'))


def pytest_collection_modifyitems(session, items):
    print("收集的测试用例:%s" % items)
    items.sort(key=lambda x: x.name)
    print("排序后收集的测试用例:%s" % items)