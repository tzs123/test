# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import allure

from common.yanl_handler import YamlHandler
from pageobject.account_page import AccountPage
from pageobject.aecard_page import AecardPage
from pageobject.login_page import LoginPage
from selenium import webdriver

class Test:
    driver = webdriver.Chrome()

    @classmethod
    def setup_class(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setup(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录")
    @allure.description('测试描述：登录成功')
    @allure.title('测试用例描述：正确的账号密码登录成功')
    def test_11(self):
        yaml_data = YamlHandler('../config/login.yaml').read_yaml()
        with allure.step("输入正确的账号密码"):
            allure.attach('13800138006，123456', name='正确账号，密码')
        aa = LoginPage(Test.driver)
        aa.test_login(yaml_data['Login']['username'],yaml_data['Login']['password'],yaml_data['Login']['Verification'])

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("积分商城")
    @allure.description('测试描述：进入积分商城界面')
    @allure.title('测试用例描述：点击积分商城')
    def test_12(self):
        with allure.step("点击积分商城"):
            allure.attach('ok', name='进入积分商城界面')
        AecardPage(Test.driver).test_aecard()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("账号余额")
    @allure.description('测试描述：进入账号余额界面')
    @allure.title('测试用例描述：点击账号余额')
    def test_13(self):
        with allure.step("点击账号余额"):
            allure.attach('ok', name='进入账号余额界面')
        AccountPage(Test.driver).test_account()

    def teardown(self):
        self.driver.get("http://testingedu.com.cn:8000/index.php/Home/User/index.html")
        self.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
