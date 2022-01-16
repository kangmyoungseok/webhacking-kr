from bs4 import BeautifulSoup
import re
from selenium import webdriver


fr = open("dictionary.txt","r")
HASH_LIST = fr.readlines()
SALT = 'salt_for_you'

params = {
    'key' : ''
}

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



def bring_problem_hash(session):
    response = session.get("https://webhacking.kr/challenge/web-04/")
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    hash_value = soup.find('b').text
    return hash_value


def find_plain_text(hash):
    for hash_str in HASH_LIST:
        plain_number = hash_str.split(":")[0]
        hash_value = hash_str.split(":")[1][:-1]
        if(hash_value == hash ):
            return plain_number
            
    return -1

def login(driver):
    driver.find_element_by_name("id").send_keys("oksusu98")
    driver.find_element_by_name("pw").send_keys("비밀번호!")
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/form/input').submit()    
    
def main():
#    session = requests.Session()
    driver = make_driver()
    driver.get('https://webhacking.kr/login.php')
# 로그인
    login(driver)

    result = -1
    while(result == -1):
        # 사전파일에 있는 해시값이 나올때 까지 웹페이지 재접속
        driver.get('https://webhacking.kr/challenge/web-04/')
        hash_value = driver.find_element_by_xpath('/html/body/center/form/table/tbody/tr[1]/td/b').text
        result = find_plain_text(hash_value)
        print(hash_value)
        print(result)
    
    # 값을 찾으면 웹사이트로 값을 보내기
    plain_text = result + SALT
    params = {'key' : plain_text}
    driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[2]/td[2]/input").send_keys(result + SALT)
    driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[2]/td[3]/input").click()
    print(params)

    driver.close()
    
if __name__ == "__main__":
    main()



