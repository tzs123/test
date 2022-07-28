# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest
from common.DBHandler import MysqlUtil
from common.excel_util import excel1, ExcelHandler
from common.loger_handler import logger
from common.yanl_handler import yaml_data1, yaml_data2
from common.request import *
from testcase import test_helper


data_res = r'C:\Users\Administrator\.jenkins\workspace\psimsendemail\untitled\report\test_report.xlsx'
data = r'C:\Users\Administrator\.jenkins\workspace\psimsendemail\untitled\data\register.xlsx'


class Test_Register():
    #读取测试数据
    execl_handle = excel1

    def setUp(self) -> None:
        self.req = HTTPHandle()
        self.db_info = yaml_data1
        self.db = MysqlUtil(self.db_info)
        self.host = yaml_data2['mockhost']
        self.logger = logger

    def tearDown(self) -> None:
        self.db.close()

    @pytest.mark.parametrize('test_data',execl_handle)
    def test_register(self,test_data):
        test_helper.copy_sheet('register')     #把register页面的测试用例内容复制到test_report结果表
        '''
        如果excel中出现了#new_phone#，则通过gen_phonenun方法生成一个手机号mobilephone，
        在数据库中查询手机号mobilephone是否存在。若不存在，则使用该号码，通过replace函数，
        将代码读取的test_data["json"]数据中的#new_phone#替换为手机号；若存在，
        则继续 while True 循环，直到生成的手机号在数据库中不出存在，跳出循环
        :param test_data:
        :return:
        '''
        if '#new_phone#' in str(test_data['json']):
            while True:
                mobilephone = test_helper.get_phonenum()
                sql1 = '''SELECT * FROM users WHERE phonenum= %s;'''
                dbphone = self.db.query(sql=sql1,args=mobilephone)
                if not dbphone:
                    break
            test_data['json'] = test_data['json'].replace('$new_phone$',mobilephone)

        '''
        如果excel中出现了#exist_phone#，则在数据库中查询一条已注册成功的手机号，通过replace函数，
        将代码读取的test_data["json"]数据中的#exist_phone#替换为手机号
        '''
        if '#exist_phone#' in str(test_data['json']):
            sql2 = '''select phonenum from users limit 1;'''
            mobilephone = self.db.query(sql=sql2)['phonenum']
            test_data['json'] = test_data['json'].replace('$exist_phone$',mobilephone)
        self.logger.info("用例名称：{};接口信息：url={}；method={}；headers={}；json={}".format(test_data["case_name"],
                                                                                   self.host + test_data["url"],
                                                                                   test_data["method"],
                                                                                   eval(test_data['headers']),
                                                                                   json.loads(test_data["json"])
                                                                                   ))

        res = self.req.visit(url=self.host+test_data['url'],
                       method=test_data['method'],
                       header=eval(test_data['headers']),
                       json = json.loads(test_data['json']))
        self.logger.info("接口响应内容：{}".format(res))
        try:
            assert res['code'] == test_data['excepted']
            self.logger.info("接口响应code:{}，期望响应code:{}".format(res["code"], test_data["excepted"]))
            ExcelHandler.write(data_res, 'register', test_data["caseid"] + 1, 9, 'passed')
        except AssertionError as e:
            self.logger.error("测试用例执行失败：{}".format(e))
            ExcelHandler.write(data_res, 'register', test_data["caseid"] + 1, 9, 'failed')
            raise e