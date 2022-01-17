from pydoc import plain
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import hashlib
import time

CHAIN_LEN = 100
fr = open("../webhacking-kr/rainbow.txt","r")
# HASH_LIST = fr.readlines()
SALT = 'salt_for_you'
HASH_LIST2 = fr.read()

def sha1_500(plain_text):
    for i in range(500):
        plain_text = hashlib.sha1(plain_text.encode("ascii")).hexdigest()
    hash_value = plain_text
    return hash_value

def reduce_function(hash):
    '''
    축소 함수 : 추출된 해시 함수로부터 다음 평문을 만든다.
    로직 : 해시값에서 숫자 8자리 추출해서 다음 평문으로 만든다.
    '''
    numbers = re.findall("\d",hash)

    # 맨 앞에서 0이 연속으로 나온 경우 3가지만 제거해 준다.
    if (numbers[0] == '0'):
        if(numbers[1] == '0'):
            if(numbers[2] == '0'):
                numbers = numbers[3:]
            else:
                numbers = numbers[2:]
        else:
            numbers = numbers[1:]

    next_plain_number = ''
    # 해시 값에 숫자가 8개 이하로 존재할 수 있는 가능성 인지하고 처리 해줄 것
    for i in range(8):
        next_plain_number +=numbers[i]

    return int(next_plain_number)


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

def trace_hash_chain(plain_number, source_hash):
#    print(plain_number)
    for i in range(CHAIN_LEN):
        hash_value = sha1_500(plain_number + SALT)
        if(hash_value == source_hash):
            return plain_number
        plain_number = str(reduce_function(hash_value))
    return 'None'


def find_plain_text(hash):
    source_hash = hash
    before_time = time.time()
    for i in range(CHAIN_LEN):
        index = HASH_LIST2.find(hash)
        if(index != -1):
            plain_number = HASH_LIST2[index-9:index-1]
            result = trace_hash_chain(plain_number,source_hash)
            # 해시 충돌에 대한 처리
            if(result != 'None'):
                return result
        # 못찾았으면 reduce function, hash를 거쳐서 다시한번 서칭
        hash =  sha1_500(str(reduce_function(hash)) + SALT)
    after_time = time.time()
    print("사전파일에서 서칭에 걸리는 시간 : {}".format(after_time-before_time))
    return -1


def login(driver):
    driver.find_element_by_name("id").send_keys("oksusu98")
    driver.find_element_by_name("pw").send_keys("비밀번호!")
    driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/form/input').submit()    
    
def main():
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

