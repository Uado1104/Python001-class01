from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver ，和浏览器的版本保持一致
    # https://chromedriver.storage.googleapis.com/index.html

    browser.get('http://www.douban.com')
    time.sleep(1)
    # 切换登陆的输入框
    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    # 找到密码登陆输入框
    btm1 = browser.find_elements_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    # 模拟鼠标点击
    btm1.click()
    # 使用xpath找到账号密码的输入栏
    btm1 = browser.find_elements_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_elements_by_id('password').send_keys('test123test456')
    time_sleep(1)
    # 使用xpath找到登陆按钮
    browser.find_elements_by_xpath('//a[contains(@class,"btn-account")]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)
except Exception as e:
    print(e)
# finally:
#     browser.close()