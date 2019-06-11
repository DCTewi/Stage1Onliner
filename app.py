#coding=utf-8

from config import *
from selenium import webdriver
import os
import time

t = 0 # nap times

def clear_scr():
    if (os.name == 'nt'):
        os.system("cls")
    else:
        os.system('clear')
    

def start_bot( page ):
    global t
    page.get('https://bbs.saraba1st.com/2b/home.php?mod=spacecp&ac=credit&showcredit=1')
    page.implicitly_wait(30)
    while True:
        try:
            # Flush page
            clear_scr()
            print("刷新页面中...", flush=True)
            page.refresh()
            page.implicitly_wait(30)
            total_point = page.find_element_by_id('extcreditmenu').text
            user_group = page.find_element_by_id('g_upmine').text

            # Print log
            clear_scr()
            print("已经挂机 " + str(t * nap_time) + " 秒, ", end='')
            print("累计 " + str(int(t * nap_time / 60 / 60)) + "小时" + str(int(t * nap_time / 60 % 60)) + "分钟" + str(int(t * nap_time % 60)) + "秒")
            print("现有积分 " + total_point + " , " + user_group, flush=True)
            print("刷新间隔: " + str(nap_time) + " 秒", flush=True)
        
            # Wait for next flush
            t += 1
            time.sleep(nap_time)
        except:
            # If page error
            clear_scr()
            print("网页故障，将会在1分钟后重试...", flush=True)
            time.sleep(60)
            page.get('https://bbs.saraba1st.com/2b/home.php?mod=spacecp&ac=credit&showcredit=1')
            page.implicitly_wait(30)

def main():
    # Init
    clear_scr()
    print("初始化界面中...", flush=True)

    # Get page
    page = webdriver.Chrome()
    page.set_window_size(1000, 800)
    page.set_window_position(800, 100)
    page.get('https://bbs.saraba1st.com/2b/forum.php')
    page.implicitly_wait(30)

    try:
        # Login
        page.find_element_by_id('ls_username').send_keys(username)
        page.find_element_by_id('ls_password').send_keys(password)
        page.find_element_by_xpath('//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em').click()
        page.implicitly_wait(30)
    except:
        print("页面初始化出现问题，请稍后重试", flush=True)
        return

    # Start upgrade
    time.sleep(3)
    start_bot(page)

if __name__ == "__main__":
    main()
