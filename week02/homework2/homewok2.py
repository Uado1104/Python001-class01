# 题目描述：使用 requests 或 Selenium 模拟登录石墨文档 https://shimo.im
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver ，和浏览器的版本保持一致
    # https://chromedriver.storage.googleapis.com/index.html

    browser.get('https://shimo.im')
    time.sleep(1)
    # 找到密码登陆输入框
    btm1 = browser.find_elements_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    # 模拟鼠标点击
    btm1.click()
    # 使用xpath找到账号密码的输入栏
    btm1 = browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input"]').send_keys('15055495@qq.com')
    browser.find_elements_by_id('password').send_keys('test123test456')
    time_sleep(1)
    # 使用xpath找到登陆按钮
    browser.find_elements_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()