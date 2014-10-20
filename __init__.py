# -*- coding: utf-8 -*-

import os
from selenium import webdriver
import time
import datetime
import requests

def hello():
	print "in __init__.py"

def send_weibo(username, password):
	user = {"username":username,"password":password}
	starttime = datetime.datetime.now()
	driver = webdriver.PhantomJS()
	# driver = webdriver.Chrome()
	driver.delete_all_cookies()
	cookies = {}

	driver.get("http://weibo.com/login.php")
	dr = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div[5]/div[1]/div/input")[0].send_keys(user['username'])
	driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div[5]/div[2]/div/input")[0].send_keys(user["password"])
	dr = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/div[5]/div[6]/div[1]/a")[0].click()
	driver.find_element_by_link_text("首页").click()
	cookies = "; ".join([item["name"] + "=" + item["value"] for item in driver.get_cookies()])
	current_url = driver.current_url
	uid = current_url.replace("http://weibo.com/u/","").replace("/home?topnav=1&wvr=5","")
	driver.close()
	driver.quit()

	headers ={
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate",
		"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
		"Cache-Control":"no-cache",
		"Connection":"keep-alive",
		"Content-Length":"98",
		"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
		"Cookie":cookies,
		"Host":"weibo.com",
		"Pragma":"no-cache",
		"Referer":"http://weibo.com/u/%s/home?leftnav=1&wvr=5&is_ori=1" % uid,
		"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0",
		"X-Requested-With":"XMLHttpRequest",
	}
	data = {
		"_surl":"",	
		"_t":0,
		"hottopicid":"",	
		"location":"home",
		"module":"stissue",
		"pic_id":"",
		"rank":0,
		"rankid":'',	
		"text":"What are you dogin?PhantomJS",	
	}
	url = "http://weibo.com/aj/mblog/add?_wv=5&__rnd=%s" % int(time.time()*1000)

	session = requests.Session()
	r = session.post(url,headers=headers,data=data)

	print datetime.datetime.now()-starttime
