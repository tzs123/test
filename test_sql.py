# _*_ coding:utf-8 _*_
import json

import allure
import pymysql


from common.yanl_handler import yaml_data


@allure.epic('测试描述'.center(30, '*'))
@allure.feature('数据库')       #模块
class TestMysql:
    @allure.story('用户故事描述：查询数据')  # 模块的功能
    @allure.description('测试描述：查询数据是否正确')
    @allure.title('测试用例描述：查询客户数据')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_mysql(self):
        db = pymysql.connect(host = yaml_data['mysql']['host'],port =yaml_data['mysql']['port'],db=yaml_data['mysql']['db'],
                             user=yaml_data['mysql']['user'],passwd=yaml_data['mysql']['passwd'],charset=yaml_data['mysql']['charset'])
        info = db.cursor()
        info.execute(yaml_data['mysql']['sql'])
        data = info.fetchall()
        ret =[]
        for one,two in data:
            line = one
            line1 = two
            ret.append([line,line1])
        print(ret)
        #结果：[['1', '董卓'], ['2', '张坤'], ['3', '王伟']]
        with allure.step("查询"):
            allure.attach('{}'.format(yaml_data['mysql']['sql']),name='sql执行')
        with allure.step("响应"):
            allure.attach('{}'.format(ret),name='返回结果')
        with allure.step("断言"):
            assert ret == yaml_data['mysql']['except']
            allure.attach('OK',name='断言成功')
