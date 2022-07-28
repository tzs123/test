# !/usr/bin/env python
# _*_ coding:utf-8 _*_

from airtest.core.api import *
import random
import re
from copy import copy
from openpyxl import load_workbook
from selenium import webdriver
data_res = r'C:\Users\Administrator\.jenkins\workspace\psimsendemail\untitled\report\test_report.xlsx'
data = r'C:\Users\Administrator\.jenkins\workspace\psimsendemail\untitled\data\register.xlsx'



def testaa():
  #点击web浏览器的百度页面的新闻按钮
  news_path = 'news.png'
  #点击web浏览器的新闻里面的网页按钮
  internet_path = 'internet.png'
  #点击pc端的qq音乐程序图标
  qq_music_path = 'qq音乐.png'
  abc_music_path = '播放.png'
  connect_device('Windows:///')
  ST.CVSTRATEGY = ["surf", "tpl"]
  ST.FIND_TIMEOUT = 2
  # touch(Template(news_path))
  # touch(Template(internet_path))
  double_click(Template(qq_music_path))
  double_click(Template(abc_music_path))
def test_start(func):
  def test123():
    aa = [55,14,35,34,74]
    func()
    for i in aa:
      if i%10==4:
        print(i)
  return test123


@test_start
def testbb():
  aa = [551, 114, 315, 314, 741]
  for i in aa:
    #输出十位上的数字
    print(i//10%10)


def test22():
  workbook = load_workbook(data)
  sheet = workbook['login']
  target = workbook.copy_worksheet(sheet)
  workbook.save(data)

