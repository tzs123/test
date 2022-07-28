# _*_ coding:utf-8 _*_

import flask,json
import pytest
# __name__,代表当前这个python文件
server = flask.Flask(__name__) #把咱们当前这个python文件，当做一个服务(启动服务)
def my_db(sql):
    import pymysql
    coon = pymysql.connect(
        host='192.168.0.219', user='root', passwd='123456',
        port=3306, db='test', charset='utf8')
    cur = coon.cursor() #建立游标
    cur.execute(sql)#执行sql
    if sql.strip()[:6].upper()=='SELECT':
        res =  cur.fetchall()
    else:
        coon.commit()
        res = 'ok'
    cur.close()
    coon.close()
    return res

@server.route('/login',methods=['post'])
def reg():
    username = flask.request.values.get('root')#
    pwd = flask.request.values.get('123456')
    print('username..',username)
    if username == 'root':
        sql = 'SELECT * from sec_name where username="%s";'%username
        # res = my_db(sql)
        if my_db(sql):
            res = {'msg':'用户已存在','msg_code':2001}
        else:
            insert_sql = 'insert into sec_name (username,passwd,is_admin) values ("%s","%s",0);'%(username,pwd)
            my_db(insert_sql)
            res = {'msg':'注册成功！','msg_code':0}
    else:
        res = {'msg':'账号或密码错误','msg_code':1001}
        # 1001必填字段未填
    return json.dumps(res,ensure_ascii=False)

server.run(port=7777,debug=True,host='0.0.0.0')  #debug=True，改了代码之后，不用重启它会自动帮你重启
if __name__ == '__main__':
    pytest.main()
#
# import pytest
# import yaml
#
# from common.request import RequestsHandler
# from common.yanl_handler import yaml_data, YamlHandler
# from string import Template
#
# class TestToken:
#     def test_get_token(self):
#         try:
#             aa = YamlHandler('../config/aaa.yaml').read_yaml()
#             req = RequestsHandler.test_request(self, method=aa['request']['method'],
#                                                url=aa['request']['url'],
#                                                headers=aa['request']['headers'],
#                                                data=aa['request']['params'])
#             ress = json.loads(req.text)
#             print(ress)
#             # print(type(ress))
#             # print(ress['code'])
#             # with open("../config/aaa.yaml", encoding='utf-8') as fp:
#             #     read_yml_str = fp.read()
#             #     # print(xx)
#             # tempTemplate1 = Template(read_yml_str)
#             # c = tempTemplate1.safe_substitute({"message":ress['message'],'token':aa['request']['headers']['Authorization'],
#             #                                    'status_code':ress['code']})
#             #
#             # print(c)
#             YamlHandler('../config/bbb.yaml').write_yaml({'request':{'token':aa['request']['headers']['Authorization']}})
#         except Exception as e:
#             print(e)








