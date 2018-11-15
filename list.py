from selenium import webdriver
import pickle
import time
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get("https://aliexpress.com")
cookies = pickle.load(open("cookies.pickle", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


def extract_product_urls_from_list_page(list_page_url):
    driver.get(list_page_url)
    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")

    for link in soup.find('ul',{'class':'items-list'}).find_all('div',{'class':'pic'}):
        print link.a['href']    

if __name__ == '__main__':
    extract_product_urls_from_list_page('https://beddingoutlet.aliexpress.com/store/group/Galaxy-Sea-Duvet-Cover-Set/1160570_512585898.html')
    #print(duvetlist)

