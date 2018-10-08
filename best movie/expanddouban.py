# coding:utf-8
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def getHtml(url, load_more=False, wait_time=2):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=option)
    browser.get(url)
    # time.sleep(wait_time)
    if load_more:
        while True:
            try:
                next_button = browser.find_element_by_class_name("more")
                click = next_button.click()
                print(click)
                time.sleep(wait_time)
            except:
                break
    html = browser.page_source
    print(html)
    browser.quit()
    return html


# for test
url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影,剧情,美国"
html = getHtml(url, True)
print(html)
"""
url: the douban page we will get html from
loadmore: whether or not click load more on the bottom 
waittime: seconds the broswer will wait after intial load and 
"""

# soup = BeautifulSoup(html, "html.parser")
# print(soup.findAll())
