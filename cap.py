# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


def get_image(url):
    chromedriver = r".\chrome\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    driver.get(url)
    time.sleep(2)
    # width = driver.execute_script("return document.documentElement.scrollWidth")
    width = 1800
    height = driver.execute_script("return document.documentElement.scrollHeight")
    title = driver.title
    print(width, height)
    driver.set_window_size(width, height)
    time.sleep(2)
    driver.save_screenshot(r".\pic\%s.png" % title)
    driver.close()


def get_dir():
    # 判断文件夹是否存在，如果不存在就创建一个
    filename = "../pics"
    if not os.path.isdir(filename):
        os.makedirs(filename)
    return filename


if __name__ == '__main__':
    f = open('url.txt', mode='r')
    line = f.readlines()
    for x in line:
        print(x)
        get_image(x)
