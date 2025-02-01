#!/usr/bin/env python3
# Sources: https://www.geeksforgeeks.org/image-scraping-with-python/
# https://www.zenrows.com/blog/scraping-javascript-rendered-web-pages#extract-html
# ChatGPT

# import necessary tools from the selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# set up chrome driver
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

# assign the target URL
targetURL = "https://ash.silverchair-cdn.com/ash/content_public/journal/bloodadvances/5/23/10.1182_bloodadvances.2021004965/2/advancesadv2021004965f2.png"

# navigate to the target webpage
driver.get(targetURL)

# wait for the content image to load
WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.CLASS_NAME, "content-image"))
    EC.presence_of_all_elements_located((By.CLASS_NAME, "content-image"))
)

# select the content image element
content_image = driver.find_element(By.CLASS_NAME, "content-image")

# print the content image element
htmlData = content_image.get_attribute("outerHTML")

# close the browser
driver.quit()

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(htmlData, 'html.parser')  

# initialize an empty dictionary for image URLs
imageURLs = {}

# add image sources to the dictionary
for index, item in enumerate(soup.find_all('img')): 
    imageURLs[f'image_{index}'] = item['src']

# iterate over the dictionary and print key-value pairs
for key, value in imageURLs.items():
    print(f"{key}: {value}")