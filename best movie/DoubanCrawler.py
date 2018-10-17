# coding:utf-8
import csv
import time
from collections import ChainMap

from bs4 import BeautifulSoup
from selenium import webdriver

douban_movie_url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags="

output_format = "category:[{}], location:[{}], count:[{}], percent:[{:.4}%]"

movie_list = set()
category_location_movie_count = {}

category_list = ["剧情", "喜剧", "动作"]

location_list = ["中国大陆", "美国", "香港", "台湾", "日本", "韩国", "英国", "法国",
                 "德国", "意大利", "西班牙", "印度", "泰国", "俄罗斯", "伊朗", "加拿大",
                 "澳大利亚", "爱尔兰", "瑞典", "巴西", "丹麦"]


def get_movie_url(category, location):
    tags = set()
    tags.add("电影")
    url = str(douban_movie_url)
    if category is not None:
        tags.add(category)
    if location is not None:
        tags.add(location)
    return url + ",".join(tags)


def get_html(url, load_more=False, wait_time=2):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    browser = webdriver.Chrome(chrome_options=option)
    browser.get(url)
    if load_more:
        while True:
            try:
                next_button = browser.find_element_by_class_name("more")
                next_button.click()
                time.sleep(wait_time)
            except:
                break
    html = browser.page_source
    browser.quit()
    return html


class movie:
    def __init__(self, name=None, rate=None, location=None, category=None, info_link=None, cover_link=None):
        self.name = name
        self.rate = rate
        self.location = location
        self.category = category
        self.info_link = info_link
        self.cover_link = cover_link


def get_movies(category=None, location=None):
    movie_url = get_movie_url(category, location)
    print(movie_url)
    movie_html = get_html(movie_url, True)
    soup = BeautifulSoup(movie_html, features="html.parser")
    movie_item = soup.find_all('a', class_="item")
    movies = set()
    for item in movie_item:
        info_link = item.attrs.get('href')
        cover_link = item.div.span.img.attrs.get('src')
        name_tag = item.p.next
        name = name_tag.next
        rate_tag = name_tag.next.next.next
        rate = rate_tag.next
        movies.add(movie(name, rate, location, category, info_link, cover_link))
    if category_location_movie_count.__contains__(category):
        category_location_movie_count[category] = ChainMap(category_location_movie_count[category],
                                                           {location: movies.__len__()})
    else:
        category_location_movie_count[category] = {location: movies.__len__()}
    return movies


for category in category_list:
    for location in location_list:
        movie_list |= get_movies(category, location)

with open('movies.csv', 'w', newline='', encoding='utf8') as movie_file:
    writer = csv.writer(movie_file)
    for movie in movie_list:
        writer.writerow(movie.__dict__.values())

location_file = open("output.txt", 'w', newline='', encoding='utf8')
for category in category_list:
    location_movie_count = sorted(category_location_movie_count.get(category).items(),
                                  key=lambda count: count[1], reverse=True)
    total = 0
    movie_dict = dict(location_movie_count)
    for location in location_list:
        total += movie_dict[location]
    for location in list(movie_dict.keys())[:3]:
        if total != 0:
            print(output_format.format(category, location, movie_dict[location],
                                       float(movie_dict[location] * 100) / float(total)),
                  file=location_file)
        else:
            print(output_format.format(category, location, movie_dict[location], float(0)), file=location_file)
location_file.flush()
