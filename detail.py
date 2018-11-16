from selenium import webdriver
import json
import pickle
from datetime import datetime
from bs4 import BeautifulSoup
import ali_config
from slugify import slugify
import pandas as pd


driver = webdriver.Firefox()
driver.get("https://aliexpress.com")
cookies = pickle.load(open("cookies.pickle", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

# remove _50x50.jpg 
def edit_image(image):
    return image.rsplit("_",1)[0]

# remove un need word     
def remove_trademark(title):  
    global item
    for ch in item.replaceList:
        if ch in title: 
            title = title.replace(ch,"")
    return ' '.join(title.split())

def extract_product_info(product_url):
    driver.get(product_url)
    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")
    global item

    #product_id = soup.find('input', {'id': 'hid-product-id'})['value']
    title = remove_trademark(soup.find('h1', {'class': 'product-name'}).text)
    handle =  slugify(title)
    size = item.size
    index = 0
    for image in soup.find('ul',{'id':'j-image-thumb-list'}).find_all('img'):
        src = edit_image(image['src'])
        if index == 0:
            yield {
                'Handle':handle,
                'title': title,
                'Body (HTML)':item.body,
                'Vendor':'',
                'Type': item.productType,
                'Tags':item.taglist,
                'Published':'TRUE',
                'Option1 Name':'Size',
                'Option1 Value':size[index][0] if len(size) > index else "",
                'Option2 Name':'',
                'Option2 Value':'',
                'Option3 Name':'',
                'Option3 Value':'',
                'Variant SKU':'',
                'Variant Grams':'',
                'Variant Inventory Tracker':'',
                'Variant Inventory Qty':50 if len(size) > index else "",
                'Variant Inventory Policy':'deny' if len(size) > index else "",
                'Variant Fulfillment Service':'manual' if len(size) > index else "",
                'Variant Price': size[index][1] if len(size) > index else "",
                'Variant Compare At Price':size[index][2] if len(size) > index else "",
                'Variant Requires Shipping':'',
                'Variant Taxable':'',
                'Variant Barcode':'',
                'Image Src' : src,
                'Image Position':index +1,   
                'Image Alt Text':'',
            }
        else:
            if (image != ""):    
                yield {
                    'Handle':handle,
                    'title': '',
                    'Body (HTML)':'',
                    'Vendor':'',
                    'Type':'',
                    'Tags':'',
                    'Published':'TRUE' if len(size) > index else "",
                    'Option1 Name':'',
                    'Option1 Value':size[index][0] if len(size) > index else "",
                    'Option2 Name':'',
                    'Option2 Value':'',
                    'Option3 Name':'',
                    'Option3 Value':'',
                    'Variant SKU':'',
                    'Variant Grams':'',
                    'Variant Inventory Tracker':'',
                    'Variant Inventory Qty':50 if len(size) > index else "",
                    'Variant Inventory Policy':'deny' if len(size) > index else "",
                    'Variant Fulfillment Service':'manual' if len(size) > index else "",
                    'Variant Price': size[index][1] if len(size) > index else "",
                    'Variant Compare At Price':size[index][2] if len(size) > index else "",
                    'Variant Requires Shipping':'',
                    'Variant Taxable':'',
                    'Variant Barcode':'',
                    'Image Src' : src,
                    'Image Position':index +1,   
                    'Image Alt Text':'',
                }     
        index += 1      
    while (index < len(size)):
        yield {
                'Handle':handle,
                'title': '',
                'Body (HTML)':'',
                'Vendor':'',
                'Type':'',
                'Tags':'',
                'Published':'TRUE',
                'Option1 Name':'',
                'Option1 Value':size[index],
                'Option2 Name':'',
                'Option2 Value':'',
                'Option3 Name':'',
                'Option3 Value':'',
                'Variant SKU':'',
                'Variant Grams':'',
                'Variant Inventory Tracker':'',
                'Variant Inventory Qty':'50',
                'Variant Inventory Policy':'deny',
                'Variant Fulfillment Service':'manual',
                'Variant Price': size[index][1] ,
                'Variant Compare At Price':size[index][2],
                'Variant Requires Shipping':'',
                'Variant Taxable':'',
                'Variant Barcode':'',
                'Image Src' : '',
                'Image Position':'',   
                'Image Alt Text':'',
        }
        index +=  1            


if __name__ == '__main__':
    item = ali_config.duvetClass()   
    productDetail = pd.DataFrame.from_records(extract_product_info('https://www.aliexpress.com/item/Hair-Accessories-Synthetic-Wig-Donuts-Bud-Head-Band-Ball-French-Twist-Magic-DIY-Tool-Bun-Maker/32457370321.html?scm=1007.13442.37932.0&pvid=f8b9f498-65d4-400f-a14f-38b4bba77546&tpp=1'))
    productDetail.to_csv("detai.csv", index = False)


