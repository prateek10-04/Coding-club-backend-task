import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver

driver=webdriver.Chrome()
url='https://www.myntra.com/'
driver.get(url)
def get_url(search_term):
    template='https://www.myntra.com/{}'
    return template.format(search_term)
url=get_url('sneakers')

headers={'Accept-Language': 'en-US,en;q=0.5'}
for pages in range(1,5):
    page=requests.get(url+'?p='+str(pages))
    soup=BeautifulSoup(page.text,'html.parser')
    shoe_data=soup.findAll('li',attrs={'class': 'product-base'})
    sleep(20)
    with open('Sneakers data.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Name', 'Category', 'Rating']
        thewriter.writerow(header)

        for store in shoe_data:
            name=store.a.find('div',class_='product-productMetaInfo').h3.text

            category_product=store.a.find('div',class_='product-productMetaInfo').find('h4',class_='product-product').text

            rating_product=store.find('div',class_='product-ratingsContainer').span.text if store.find('div',class_='product-ratingsContainer').span else "###"

            info = [name, category_product, rating_product]
            thewriter.writerow(info)






