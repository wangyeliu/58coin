#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from  selenium import  webdriver
import time


driver =  webdriver.Chrome()
driver.get('http://agent.test.58ex.com/#/login')

driver.maximize_window() #窗口最大化

driver.implicitly_wait(10)
#insdev名字的路由器换成dev5   密码58btc@tianbi了

def test():
    name = '13800002222'
    password = '12345678'

    driver.find_element_by_class_name('el-input__inner').send_keys(name)

    driver.find_element_by_css_selector("[placeholder='请输入密码']").send_keys(password)

    driver.find_element_by_css_selector("[style='width: 100%; opacity: 1;']").click()
    time.sleep(10)

    #点击经纪人机构（默认打开的就不用点击了）
    #driver.find_element_by_css_selector("[class='el-submenu__icon-arrow el-icon-arrow-down']").click()

    #点击客户列表
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/div/ul/div[4]/li/ul/li/ul/li[1]').click()
    time.sleep(3)
    #选择客户类型
    driver.find_element_by_css_selector("[placeholder='请选择']").click()

    #选择用户
    driver.find_element_by_css_selector('body > div.el-select-dropdown.el-popper > div.el-scrollbar >'
                                        ' div.el-select-dropdown__wrap.el-scrollbar__wrap.el-scrollbar__'
                                        'wrap--hidden-default > ul > li:nth-child(3)').click()
    #点击搜索

    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div[2]/div/button[1]/span').click()
    time.sleep(1)

    #点击收益记录
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/div/ul/div[4]/li/ul/li/ul/li[2]').click()
    #点击经纪人账户
    driver.find_element_by_css_selector("[placeholder='请输入经纪人账号']").send_keys('14766666666')

    #点击是否结算
    driver.find_element_by_css_selector("[class='el-radio__inner']").click()

    #点击搜索
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div[2]/div/button[1]').click()
    time.sleep(5)

    #点击经纪人管理
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/aside/div/ul/div[4]/li/ul/li/ul/li[3]').click()
    time.sleep(2)

    #输入经纪人账户
    driver.find_element_by_css_selector("[placeholder='请输入经纪人账号']").send_keys('14899999999')

    #点击搜索按钮

    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div/form/div[3]/div/button[1]').click()

    time.sleep(5)
    #查询后修改返佣比例，点击修改操作
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div/div[1]/div/div[3]/table/tbody/tr/td[8]/div/span[1]').click()

    # 修改一级返佣比例
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath(
        '//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/input').send_keys('30')
    #修改多级返佣
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[3]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[3]/div/div/input').send_keys('50')


    #修改KPI

    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[4]/div/div/input').clear()
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[4]/div/div/input').send_keys('2')


    #点击提交
    driver.find_element_by_css_selector("[class='footer-alert']").click()
    time.sleep(5)

    #点击删除按钮
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div/div[1]/div/div[3]/table/tbody/tr/td[8]/div/span[2]').click()

    #点击确定
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
    time.sleep(3)

    #点击新增经纪人

    driver.find_element_by_css_selector("[class='el-icon-plus']").click()

    #输入经纪人账户

    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[1]/div/div/input').send_keys('14899999999')
    #输入一级返佣比例
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/input').send_keys('30')
    #多级返佣比例
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[3]/div/div/input').send_keys('50')
    #设置KPI
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[2]/form/div[4]/div/div/input').send_keys('2')
    #点击提交按钮
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/section/main/div/div/div/div[2]/div/div[3]/button').click()

    time.sleep(5)

    driver.quit()

test()





