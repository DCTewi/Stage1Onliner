#coding=utf-8

from config import *
from selenium import webdriver
import os
import time

def clear_scr():
    os.system("cls")

def start_bot( page ):
    t = 0
    while True:
        # Flush page
        clear_scr()
        print("刷新页面中...", flush=True)
        page.get('https://bbs.saraba1st.com/2b/forum-75-1.html')
        total_point = page.find_element_by_id('extcreditmenu').text
        page.implicitly_wait(5)

        # Print log
        clear_scr()
        print("已经挂机 " + str(t * nap_time) + " 秒, ", end='')
        print("累计 " + str(int(t * nap_time / 60 / 60)) + "小时" + str(int(t * nap_time / 60)) + "分钟" + str(int(t * nap_time % 60)) + "秒")
        print("现有积分 " + total_point, flush=True)
        print("刷新间隔: " + str(nap_time) + " 秒", flush=True)
        
        # Wait for next flush
        t += 1
        time.sleep(nap_time)

def main():
    # Init
    clear_scr()
    print("初始化界面中...", flush=True)

    # Get page
    page = webdriver.Chrome()
    page.set_window_size(1000, 800)
    page.set_window_position(800, 100)
    page.get('https://bbs.saraba1st.com/2b/forum.php')
    page.implicitly_wait(10)

    # Login
    page.find_element_by_id('ls_username').send_keys(username)
    page.find_element_by_id('ls_password').send_keys(password)
    page.find_element_by_xpath('//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em').click()
    page.implicitly_wait(5)

    # Start upgrade
    time.sleep(5)
    start_bot(page)

if __name__ == "__main__":
    main()
