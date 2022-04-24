# _*_ coding:utf-8 _*_

import allure
import pytest
import os
@allure.epic('测试描述'.center(30, '*'))
@allure.feature('测试模块')
@allure.suite('测试套件')
class XiaoMing:
    first_name = '明'
    last_name = '小'
    @property
    @allure.story('用户故事描述：用例3')
    @allure.title('测试标题：用例3')
    @allure.description('测试用例描述：用例3')
    @allure.testcase('http://www.baidu.com/')
    @allure.tag('测试用例标签：用例3')
    def full_name(self):
        return self.last_name + self.first_name+"回家了"

xiaoming = XiaoMing()
print(xiaoming.full_name)

@allure.epic('测试描述'.center(30, '*'))
@allure.feature('测试模块')
@allure.suite('测试套件')
class XiaoMing:
    @staticmethod
    @allure.story('用户故事描述：用例4')
    @allure.title('测试标题：用例4')
    @allure.description('测试用例描述：用例4')
    @allure.testcase('http://www.baidu.com/')
    @allure.tag('测试用例标签：用例4')
    def say_hello():
        print('同学你好')

XiaoMing.say_hello()

@allure.epic('测试描述'.center(30, '*'))
@allure.feature('测试模块')
@allure.suite('测试套件')
class XiaoMing:
    name = '小明'
    @classmethod
    @allure.story('用户故事描述：用例5')
    @allure.title('测试标题：用例5')
    @allure.description('测试用例描述：用例5')
    @allure.testcase('http://www.baidu.com/')
    @allure.tag('测试用例标签：用例5')
    def say_hello(cls):
        print('同学你好， 我是' + cls.name)
        print(cls)

XiaoMing.say_hello()

if __name__ == "__main__":
    pytest.main(['333.py', '-s','-q', '--alluredir', '../report/tmp'])
    os.system('allure generate ../report/tmp -o ../report/html --clean')

