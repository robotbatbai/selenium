import pickle
from selenium import webdriver

browser = webdriver.Firefox()

def get_cookies():
    browser.get("https://www.aliexpress.com")
    print('input your username and passowrd in firefox and hit submit')
    input('Hit enter here if you summited the form: <Enter>')
    cookies= browser.get_cookies()
    pickle.dump(cookies,open("cookies.pickle","wb"))

def set_cookies():
    browser.get("https://aliexpress.com")
    cookies = pickle.load(open("cookies.pickle","wb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get("https://bestselling.aliexpress.com/en")

if __name__ == '__main__':
    get_cookies()
