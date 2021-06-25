#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:25:30 2019

@author: sinnoha
"""

import re
import os
import requests
from bs4 import BeautifulSoup
from lxml import etree
import execjs
from functools import wraps



def logging(func):
    @wraps(func)
    def decorator(url):
        print('{:s} {:s} is downloading...'.format(chapter.string, img.split('/')[-1]))
        func(url)
        with open(main_path + '/logging.txt', 'a') as log:
            flag and log.write('{:s} {:s} downloaded ^-^'.format(chapter.string, img.split('/')[-1]) + '\n')
        flag and print('{:s} {:s} downloaded ^-^'.format(chapter.string, img.split('/')[-1]))
    return decorator

def get_html(url):
    res = requests.get(url, headers = headers, timeout = 3)
    if res.status_code == 200:
        res.encoding = 'UTF-8'
        return BeautifulSoup(res.text, 'lxml')
    else:
        res.raise_for_status

@logging
def download_img(url):
    img_index = img_url + '/' + url
    res = requests.get(img_index, headers = headers, timeout = 3)
    if res.status_code == 200:
        res.encoding = 'UTF-8'
        with open('{:s}'.format(url.split('/')[-1]), 'wb+') as f:
            f.write(res.content)
    else:
        global flag
        flag = 0
        res.raise_for_status

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
            'Referer': 'https://manhua.dmzj.com/wodebaihenaigongzuoshiye/'
            }


url = 'https://manhua.dmzj.com'
img_url = 'https://images.dmzj.com'
manga_url = '/wodebaihenaigongzuoshiye/'
soup = get_html(url + manga_url)
title = soup.title.string[:6]
path = '/Users/Sinnoha/Desktop'
main_path = path + '/' + title
not os.path.exists(main_path) and os.mkdir(main_path)
os.chdir(main_path)

chapters = soup(class_ = "cartoon_online_border")[0].find_all('a', href = re.compile('/wodebaihenaigongzuoshiye'))

for chapter in chapters:
    chapter_index = url + chapter['href']
    current_path = path + '/' + title + '/' + chapter.string
    not os.path.exists(current_path) and os.mkdir(current_path)
    os.chdir(current_path)
    js =  get_html(chapter_index).find('script')
    ctx = execjs.compile(js.string)
    imgs = ctx.eval('arr_pages')
    for img in imgs:
        try:
            flag = 1
            download_img(img)
        except requests.exceptions.RequestException:
            with open(main_path + '/logging.txt', 'a') as log:
                log.write('\n' + '*' * 25 + 'ERROR' + '*' * 25 + '\n')
                log.write('{:s} {:s} download Failed!'.format(chapter.string, img.split('/')[-1]) + '\n')
                log.write('Here is the img_url: {:s}'.format(img_url + '/' + img))
                log.write('\n' + '*' * 25 + 'ERROR' + '*' * 25 + '\n' + '\n')

    #check the num of downloaded imgs
    if len([i for i in os.listdir(current_path) if 'jpg' in i.lower()]) != len(imgs):
        with open(main_path + '/logging.txt', 'a') as log:
            log.write('\n' + '*' * 25 + 'ERROR' + '*' * 25 + '\n')
            log.write('There should be {:d} imgs while it has {:d} imgs!'
                      .format(len(imgs), len([i for i in os.listdir(current_path) if '.jpg' or '.JPG' in i])) + '\n')
            log.write('*' * 25 + 'ERROR' + '*' * 25 + '\n' + '\n')
            
print('Download Finished!')