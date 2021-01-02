from selenium import webdriver
import os
import json
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

searchterm = '장동건'
url = "https://www.google.co.kr/search?hl=ko&tbm=isch&source=hp&biw=1036&bih=646&ei=rQvvX_jEO7WGr7wPruSvoA8&q=" + searchterm + "&gs_lcp=CgNpbWcQAzIFCAAQsQMyCAgAELEDEIMBMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQM6BAgAEANQtQJYvAdghghoAHAAeACAAU-IAfICkgEBNZgBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ved=0ahUKEwi4z93f1PrtAhU1w4sBHS7yC_QQ4dUDCAc&uact=5&tbs=itp:face"
browser = webdriver.Chrome('./chromedriver')
browser.get(url)

counter = 0
succounter = 0

if not os.path.exists('images'):
    os.mkdir("images")

if not os.path.exists('preproc_images'):
    os.mkdir("preproc_images")

if not os.path.exists("images/" + searchterm):
    os.mkdir("images/" + searchterm)

for _ in range(200):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.execute_script("window.scrollBy(0,10000)")
    try:
        browser.find_element_by_css_selector(".mye4qd").click()
    except:
        continue

for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
    try:
        x.click()
        time.sleep(1)
        img_url = browser.find_element_by_xpath(
            '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute(
            "src")
        print(img_url)
    except:
        continue

    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(img_url, "images/" + searchterm + '/' + searchterm + str(counter) + '.jpg')
        counter = counter + 1
        succounter = succounter + 1
        print(succounter)
    except:
        print("can't get img")

print(succounter, "succesfully downloaded")

browser.close()
