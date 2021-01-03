from selenium import webdriver
import os
from multiprocessing import Process
import json
from selenium.webdriver.common.keys import Keys
import urllib.request
import time

# 사람당 이미지의 최대 갯수
mx_image_count = 2
base_url = "https://www.google.co.kr/search?hl=ko&tbm=isch&source=hp&biw=1036&bih=646&ei=rQvvX_jEO7WGr7wPruSvoA8&q="
base_face_image_find_url = "&gs_lcp=CgNpbWcQAzIFCAAQsQMyCAgAELEDEIMBMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQM6BAgAEANQtQJYvAdghghoAHAAeACAAU-IAfICkgEBNZgBAKABAaoBC2d3cy13aXotaW1n&sclient=img&ved=0ahUKEwi4z93f1PrtAhU1w4sBHS7yC_QQ4dUDCAc&uact=5&tbs=itp:face"

# 찾을 연예인
search_terms = ['원빈', '장동건', '강동원', '현빈', '정우성', '송중기', '차은우', '소지섭', '조인성']


def image_counter(counter):
    if counter > mx_image_count-1:
        return False
    return True


def headless_driver_option_setting(flag):
    options = webdriver.ChromeOptions()

    if flag == 1:
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

    return options


def is_path_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def is_image_preproc_images_path_exist(search_term):
    is_path_exists("images")
    is_path_exists("preproc_images")
    is_path_exists("images/" + search_term)


def crawling_start(term):
    search = term
    url = base_url + search + base_face_image_find_url
    options = headless_driver_option_setting(1)
    browser = webdriver.Chrome('./chromedriver', options=options)
    browser.get(url)

    counter = 0
    succounter = 0

    is_image_preproc_images_path_exist(search)

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
            urllib.request.urlretrieve(img_url, "images/" + search + '/' + search + str(counter) + '.jpg')
            counter = counter + 1
            succounter = succounter + 1
            if not image_counter(succounter):
                browser.close()
                return 1
            print(term + succounter)
        except:
            print("can't get img")

    print(term, succounter, "succesfully downloaded")
    browser.close()


if __name__ == "__main__":

    threads = []
    for search_term in search_terms:
        thread = Process(target=crawling_start, args=(search_term,))
        thread.start()
        threads.append(thread)

    for i in threads:
        i.join()
