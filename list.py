from selenium import webdriver
import pickle
import time
from bs4 import BeautifulSoup
import ali_config
from slugify import slugify
import pandas as pd


driver = webdriver.Firefox()
driver.get("https://aliexpress.com")
cookies = pickle.load(open("cookies.pickle", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

def extract_product_urls_from_list_page(list_page_url):
    driver.get(list_page_url)
    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")
    domain = "https:"
    for link in soup.find('ul',{'class':'items-list'}).find_all('div',{'class':'pic'}):
        time.sleep(2)
        extract_product_info(domain+link.a['href'])

    next_page = soup.find('a',{'class':'ui-pagination-next'}) 
    if next_page:
        time.sleep(2)
        extract_product_urls_from_list_page(domain + next_page['href'])

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
    global products_list
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
            product_list.append({
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
            })
        else:
            if (image != ""):    
                product_list.append({
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
                })     
        index += 1      
    while (index < len(size)):
        product_list.append({
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
        })
        index +=  1 

if __name__ == '__main__':
    item = ali_config.duvetClass()   
    product_list = []
    extract_product_urls_from_list_page('https://beddingoutlet.aliexpress.com/store/group/Galaxy-Sea-Duvet-Cover-Set/1160570_512585898.html')
    products = pd.DataFrame.from_records(product_list)
    products.to_csv("products.csv", index = False)

