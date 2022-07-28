# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import allure

# from pageobject.account_page import AccountPage
# from pageobject.aecard_page import AecardPage
# from pageobject.login_page import LoginPage
# from selenium import webdriver
# if __name__ == '__main__':
#     aa = webdriver.Chrome()
#     LoginPage(aa).test_login()
#     AecardPage(aa).test_aecard()
#     AccountPage(aa).test_account()
#     aa.quit()
import pytest
from common.utils import case_path,report_path,get_time
t = get_time()  #获取当前时间
pytest.main(['-v',f'--html={report_path}/{t}.html',case_path])