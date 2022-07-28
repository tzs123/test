# _*_ coding:utf-8 _*_
import time

import allure
from appium import webdriver


@allure.epic('测试描述'.center(30, '*'))
@allure.feature('QQ音乐')       #模块
class Test:
    def setup(self):
        desired_caps = {"deviceName": '127.0.0.1:62001',
                        'platformName': 'Android',
                        'platformVersion': '7.1.2',
                        'appPackage': 'com.android.launcher3',
                        'appActivity': '.launcher3.Launcher',
                        'unicodekeyboard': True,
                        'resetkeyboard': True
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@text="QQ音乐"]').click()
        self.driver.implicitly_wait(20)
    # @pytest.mark.parametrize('name',["11"])
    @allure.story('用户故事描述：播放音乐')  # 模块的功能
    @allure.description('测试标题：播放音乐')
    @allure.title('测试用例描述：播放音乐：我爱他')
    @allure.severity(allure.severity_level.NORMAL)
    def test_08(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/ce8"]').click()
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/eng"]').clear()
        self.driver.implicitly_wait(20)
        with allure.step("输入音乐名称"):
            allure.attach('{}'.format('我爱他'),name='音乐名称')
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/eng"]').send_keys('我爱他')
        self.driver.implicitly_wait(20)
        self.driver.keyevent(66)#66代表键盘enter
        self.driver.implicitly_wait(20)
        with allure.step("点击播放"):
            allure.attach('{}'.format('ok'),name='播放成功')
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/epe"]').click()
        self.driver.implicitly_wait(20)
        name = self.driver.find_element_by_xpath('//*[@content-desc="王小帅"]').text
        with allure.step("断言"):
            assert '王小帅' in name
            allure.attach('{}'.format('ok'),name='断言成功')
        self.driver.keyevent(4)
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.qqmusic:id/ch6"]').click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)

    def teardown(self):
        self.driver.quit()