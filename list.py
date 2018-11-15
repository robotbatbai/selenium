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
    next_page = soup.find('a',{'class':'ui-pagination-next'}) 
    if next_page:
        time.sleep(3)
        print("--------------trang2---------------")
        domain = "https:"
        extract_product_urls_from_list_page(domain + next_page['href'])
    else:
        return

if __name__ == '__main__':
    extract_product_urls_from_list_page('https://beddingoutlet.aliexpress.com/store/group/Dreamcatcher-Duvet-Cover-Set/1160570_513026552.html')
    #print(duvetlist)

