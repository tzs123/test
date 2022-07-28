# !/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
# File       : test_two.py
# Time       ：2021/11/22 20:36
# Author     ：tzs
# version    ：python 3.6
# Description：
'''

import allure

from selenium import webdriver

from common.yanl_handler import YamlHandler
from pageobject.login_page import LoginPage


@allure.epic("xxx测试")
@allure.feature("登录模块")
class Test:
    driver = webdriver.Chrome()
    yaml_data = YamlHandler('../config/login.yaml').read_yaml()

    @classmethod
    def setup_class(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：错误的账号登录失败')
    @allure.title('测试用例描述：错误的账号登录失败')
    def test_21(self):
        with allure.step("输入错误的账号"):
            allure.attach('{}'.format(Test.yaml_data['Login1']['username']), name='错误的账号')
        aa = LoginPage(Test.driver)
        aa.test_login(Test.yaml_data['Login1']['username'], Test.yaml_data['Login1']['password'],
                      Test.yaml_data['Login1']['Verification'])

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：错误的密码登录失败')
    @allure.title('测试用例描述：错误的密码登录失败')
    def test_22(self):
        with allure.step("输入错误的密码"):
            allure.attach('{}'.format(Test.yaml_data['Login2']['password']), name='错误的密码')
        aa = LoginPage(Test.driver)
        aa.test_login(Test.yaml_data['Login2']['username'], Test.yaml_data['Login2']['password'],
                      Test.yaml_data['Login2']['Verification'])

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：错误的验证码登录失败')
    @allure.title('测试用例描述：错误的验证码登录失败')
    def test_23(self):
        with allure.step("输入错误的验证码"):
            allure.attach('{}'.format(Test.yaml_data['Login3']['Verification']), name='错误的验证码')
        aa = LoginPage(Test.driver)
        aa.test_login(Test.yaml_data['Login3']['username'], Test.yaml_data['Login3']['password'],
                      Test.yaml_data['Login3']['Verification'])

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：正确的账号密码登录成功')
    @allure.title('测试用例描述：正确的账号密码登录成功')
    def test_24(self):
        with allure.step("输入正确的账号密码"):
            allure.attach('13800138006，123456', name='正确账号，密码')
        aa = LoginPage(Test.driver)
        aa.test_login(Test.yaml_data['Login']['username'], Test.yaml_data['Login']['password'],
                      Test.yaml_data['Login']['Verification'])

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



    # @pytest.mark.parametrize("username,password,verify_code",[(1,2,2),(2,5,6)])
    # def test_04(self,action):
        # while True:
        #     for i in range(4):
        #         try:
        #
        #             with allure.step("输入账号"):
        #                 allure.attach('{}'.format(excel[i]['username']), name='账号')
        #             self.driver.find_element_by_id("verify_code").clear()
        #             time.sleep(2)
        #             self.driver.find_element_by_id("username").clear()
        #             self.driver.find_element_by_id("username").send_keys(excel[i]['username'])
        #             with allure.step("输入密码"):
        #                 allure.attach('{}'.format(excel[i]['password']), name='密码')
        #             self.driver.find_element_by_id("password").clear()
        #             self.driver.find_element_by_id("password").send_keys(excel[i]['password'])
        #             with allure.step("输入验证码"):
        #                 allure.attach('{}'.format(excel[i]['verify_code']), name='验证码')
        #             self.driver.find_element_by_id("verify_code").clear()
        #             self.driver.find_element_by_id('verify_code').send_keys(excel[i]['verify_code'])
        #             # self.driver.find_element_by_name(
        #             #     'sbtbutton').click()
        #             current_handle = self.driver.current_window_handle
        #             self.driver.switch_to_window(current_handle)
        #             self.driver.find_element_by_name(
        #                 'sbtbutton').click()
        #             # 隐式等待10s
        #             self.driver.implicitly_wait(10)
        #             allhandles = self.driver.window_handles
        #             for handles in allhandles:
        #                 if handles != current_handle:
        #                     self.driver.switch_to_window(handles)
        #             self.driver.find_element_by_class_name('layui-layer-btn0').click()
        #             allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        #             self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').click()
        #             break
        #         except:
        #             continue
        #     break

        # while True:
        #     try:
        #         acode = int(input('请输入验证码:'))
        #         self.driver.find_element_by_id('verify_code').send_keys(acode)
        #         self.driver.find_element_by_name(
        #             'sbtbutton').click()
        #         # assert self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/a[1]').text()=="Stephen11111"
        #         break
        #     except:
        #         print("验证码不能为空")
        #         continue
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/ul/li[1]/a').click()
        # #鼠标光标悬浮在标签上
        # time.sleep(2)
        # ele = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/a')
        # ActionChains(self.driver).move_to_element(ele).perform()
        # ele1 = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[1]/h3/div/a')
        # ActionChains(self.driver).move_to_element(ele1).perform()
        # current_handle = self.driver.current_window_handle
        # self.driver.switch_to_window(current_handle)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/div[1]/div[2]/dl[1]/dd/a[6]').click()
        # # 隐式等待10s
        # self.driver.implicitly_wait(10)
        # # 获取当前所有窗口句柄
        # allhandles = self.driver.window_handles
        # for handles in allhandles:
        #     if handles != current_handle:
        #         self.driver.switch_to_window(handles)
        # self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[1]/a/img').click()


