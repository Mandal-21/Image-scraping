import os
import shutil
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


# header
# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
# }

# image name
# name = input("What kind of image you want to download : ")
# choice = int(input("How many number of images do you want to download : "))


def image_scrape(name, choice):
    # removing existing directory
    # dir_path = './images/' + name
    dir_path = './static/' + name

    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))


    PATH = "./chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.set_window_position(0,-1000)


    # images_urls_list
    img_collection = []

    url = 'https://www.google.co.in/search?q=' + name + '&source=lnms&tbm=isch'

    # url = "https://www.google.com" 

    driver.get(url)
    # print(driver.title)

    # search = driver.find_element_by_name("q")   # Search name
    # search.send_keys(name)    # word you want to write on search bar
    # search.send_keys(Keys.RETURN)   # for getting result we have to press ENTER (RETURN)




    # Source Page
    # print(driver.source_page)  

    """click"""
    # clicking_image = driver.find_element_by_link_text("Images")
    # clicking_image.click()


    # Thumbnail
    thumbnail_result = driver.find_elements_by_css_selector("img.Q4LuWd")
    print(len(thumbnail_result))

    # Checking no of images to be downloaded
    if choice > len(thumbnail_result):
        # Scolling to bottom of the page to load image
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    driver.implicitly_wait(5)

    # looping images
    for i in range(len(thumbnail_result)):
        try:
            thumbnail_result[i].click()
        
            image_scr = driver.find_elements_by_css_selector("img.n3VNCb")
            for image in image_scr:
                try:
                    if image.get_attribute("src") and "http" in image.get_attribute("src"):
                        img_collection.append(image.get_attribute("src"))

                except Exception as e:
                    print("image ERROR : ", e)
            
            if len(img_collection) > choice:
                break

        except Exception as e:
            print("img_scr ERROR : ", e)


    # path  
    parent = "./static/"

    file_path = parent + name + "/"
        
    try:  
        os.mkdir(file_path)  
    except OSError as error:  
        print(error)

    # downloading image
    for i in range(len(img_collection)):
        try:
            filename = name + '_{}.jpg'.format(i)
            print(filename)
            full_path = '{}{}'.format(file_path, filename) 
            urllib.request.urlretrieve(img_collection[i], full_path)
        except:
            pass


    # time.sleep(5)

    driver.close()

# https://www.google.com/search?tbm=isch&q=cat
# D:\Backup 02-27-2019\Desktop\Image_scaping\