import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def make_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])   #로그 끄기
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.67 Safari/537.36')
#    chrome_options.add_argument('--headless') #UI를 띄우지 않고 Background에서 동작
    return chrome_options

#make_driver() returns Webdriver 
def make_driver():
    chrome_options = make_options()
    driver = webdriver.Chrome('./chromedriver.exe',options=chrome_options)
    return driver

def login(driver):
    driver.get("https://webhacking.kr/login.php")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'submit')))
    driver.find_element_by_name("id").send_keys("oksusu98")
    driver.find_element_by_name("pw").send_keys("비밀번호!")
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/form/input').submit()    
    
def main():
    driver = make_driver()
    login(driver)
    driver.get("https://webhacking.kr/challenge/code-4/")

    captcha_element = driver.find_element_by_name("captcha_")
    captcha = captcha_element.get_attribute("value")

    driver.find_element_by_name("id").send_keys("oksusu")
    driver.find_element_by_name("cmt").send_keys("good example for selenium")
    driver.find_element_by_name("captcha").send_keys(captcha)
    driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td[1]/input").click()
    sleep(10)


if __name__ == '__main__':
    main()
