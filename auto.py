#! coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


name = ''
password = ''
driver = webdriver.PhantomJS()
driver.get("https://passport.jd.com/new/login.aspx")
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/a').click()
elem_account = driver.find_element_by_name("loginname")
elem_password = driver.find_element_by_name("nloginpwd")
elem_account.clear()
elem_password.clear()
elem_account.send_keys(name)
elem_password.send_keys(password)
driver.find_element_by_id("loginsubmit").click()
js='window.open("https://try.jd.com/activity/getActivityList?page=1&activityType=1&activityState=0");'
driver.execute_script(js)
time.sleep(1)
driver.switch_to_window(driver.window_handles[-1])
page = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b').text
for p in range(1, int(page) + 1):
    js='window.open("https://try.jd.com/activity/getActivityList?page=%s&activityType=1&activityState=0");' % str(p)
    driver.execute_script(js)
    driver.switch_to_window(driver.window_handles[-1])
    time.sleep(1)
    for i in range(1, 21):
        try:
            driver.switch_to_window(driver.window_handles[-1])
            try:
                xpath = '//*[@id="goods-list"]/div[2]/div/ul/li[%s]/div/a' % str(i)
                driver.find_element_by_xpath(xpath).click()
            except:
                continue
            driver.switch_to_window(driver.window_handles[-1])
            driver.find_element_by_xpath('//*[@id="btn-app"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[10]/div/div/a').click()
            time.sleep(1)
        except:
            driver.switch_to_window(driver.window_handles[-1])
            driver.close()
            continue
        driver.switch_to_window(driver.window_handles[-1])
        driver.close()

    driver.switch_to_window(driver.window_handles[-1])
