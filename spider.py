from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
import re
import random
import csv

waitTime = 10

list = []

def setDriver():
    chromeOptions = Options()
    # chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--disable-gpu")

    service_args = [
        '--proxy=113.240.226.164:8080',
        '--proxy-type=HTTPS',
    ]


    driver = webdriver.Chrome(options=chromeOptions)
    # driver = webdriver.PhantomJS()


    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "accept-language": "zh-CN,zh;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "cache-control": "max-age=0",
        "cookie": "GSP=LM=1546602202:S=VZQ5hifSnyxZyeJE; NID=154=nrSWp91PzJLuYrlWZQpbwkGu0d8kdTfWTutErx-JL-WKZcq8RLmnjNvgU9FgmMkG2Q1d50HRli0lBqShJ2qKcIjCWPuGVCVWCuKeFMDfx8wSDkBsuaFRBes8iPvysjCwpTiL5miwXoGRa3pgnfjguVHGVTKYSKpiPc7VS_kwtnM; GOOGLE_ABUSE_EXEMPTION=ID=e4e7fb6c5a57fd72:TM=1546602449:C=r:IP=178.128.50.186-:S=APGng0ukIsotjmsSSx-sBxDIAqlsbKrhbA",
        "refer": "https://www.google.com/sorry/index?continue=https://scholar.google.com/citations%3Fuser%3DTEC3pGAAAAAJ%26amp%3Bhl%3Den%26amp%3Boi%3Dsra&q=EgSygDK6GNGPveEFIhkA8aeDS9ErJH21QjnDYE-X94vBXdCVl9ypMgFy"
    }

    for key, value in enumerate(headers):
        capability_key = 'phantomjs.page.customHeaders.{}'.format(key)
        webdriver.DesiredCapabilities.PHANTOMJS[capability_key] = value

    return driver

if __name__ == '__main__':

    with open('cite_link.txt', 'r') as f:
        link_list = f.readlines()

    driver = setDriver()

    for index, root_link in enumerate(link_list):
        if index == 53 or index <= 49:
            continue
        root_link = root_link.strip()
        for step in range(0, 100000, 10):
            title_list = []
            link = root_link + '&start=' + str(step)
            print(link)
            driver.get(link)
            driver.implicitly_wait(waitTime)
            time.sleep(random.random()+10)
            # print(driver.page_source)
            
            title_hrefs = driver.find_elements_by_class_name('gs_rt')
            if len(title_hrefs) > 1:
                for title_index, title_href in enumerate(title_hrefs):
                    if title_index == 0:
                        continue
                    try:
                        title = title_href.find_element_by_tag_name('a').text
                    except:
                        title = title_href.find_elements_by_tag_name('span')[-1].text
                    title_list.append(title+'\n')
                    print(step+title_index, title)
            
                with open(str(index)+'.txt', 'a', encoding='utf-8') as f:
                    f.writelines(title_list)
            else:
                with open(str(index)+'.txt', 'a', encoding='utf-8') as f:
                    f.writelines(title_list)
                break
            
