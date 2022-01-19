import requests
from bs4 import BeautifulSoup
import time
import hashlib
import re
#초기 설정들
BASE_URL = "https://webhacking.kr/challenge/bonus-6/"
LINK_RE = '[a-z0-9]+\.php'

#로그인
def login(session):
    datas = {}
    print(" ------------ login ----------------------")
    datas['id'] = input("webhacking.kr id: ")
    datas['pw'] = input("webhacking.kr pw: ")
    response = session.post("https://webhacking.kr/login.php?login",data=datas)
    if( "<script>location.href='/';</script>" in response.text):
        print("login success : ",datas['id'])
    else:
        print("login Fail")
        exit(0)


def get_link(response):
    soup = BeautifulSoup(response.text,'html.parser').find_all('a')
    m = re.search(LINK_RE,str(soup[1]))
    return m.group()

#33-1
def solve_1(session):
    response = session.get("https://webhacking.kr/challenge/bonus-6/?get=hehe")
    next_link = get_link(response)
    print("solve 33-1 :",next_link)
    return next_link

#33-2
def solve_2(session,next_link):
    url = BASE_URL + next_link
    datas = {
        'post' : 'hehe',
        'post2' : 'hehe2'
    }
    response = session.post(url,data= datas)
    next_link = get_link(response)
    print("solve 33-2 :",next_link)
    return next_link

#33-3
def solve_3(session,next_link):
    url = BASE_URL + next_link
    params = {
        'myip' : ip
    }

    response = session.get(url,params=params )
    next_link = get_link(response)
    print("solve 33-3 :",next_link)
    return next_link
#33-4
def solve_4(session,next_link):
    url = BASE_URL + next_link
    current_time = int(time.time())
    md5_time = hashlib.md5(str(current_time).encode("ascii")).hexdigest()
    params = {
        'password' : md5_time
    }

    response = session.get(url,params=params)
    next_link = get_link(response)
    print("solve 33-4 :",next_link)
    return next_link
#33-5
def solve_5(session,next_link):
    url = BASE_URL + next_link
    params = {'imget': '1' }
    datas = {'impost': '1'}
    cookies = {'imcookie':'1'}

    response = session.post(url,data=datas,params=params,cookies=cookies)
    next_link = get_link(response)
    print("solve 33-5 :",next_link)
    return next_link
#33-6
def solve_6(session,next_link):
    url = BASE_URL + next_link

    cookie_test = hashlib.md5(ip.encode('ascii')).hexdigest()
    cookies = {'test' : cookie_test}

    my_user_agent = session.headers['User-Agent']
    data_kk = hashlib.md5(my_user_agent.encode('ascii')).hexdigest()
    data = {'kk':data_kk}

    response = session.post(url,cookies=cookies,data=data)
    next_link = get_link(response)
    print("solve 33-6 :",next_link)
    return next_link
#33-7
def solve_7(session,next_link):
    url = BASE_URL + next_link

    replaced_ip = ip.replace('.','')
    params = {replaced_ip : replaced_ip}

    response = session.get(url,params=params)
    next_link = get_link(response)
    print("solve 33-7 :",next_link)
    return next_link
#33-8
def solve_8(session,next_link):
    url = BASE_URL + next_link
    params = {'addr' : '127.0.0.1'}

    response = session.get(url,params=params)
    next_link = get_link(response)
    print("solve 33-8 :",next_link)
    return next_link

#33-9
def solve_9(session,next_link):
    url = BASE_URL + next_link
    answer = ''
    for i in range(97,123,2):
        answer += chr(i)
    params = {'ans':answer}

    response = session.get(url,params=params)
    next_link = get_link(response)
    print("solve 33-9 :",next_link)
    return next_link
#33-10
def solve_10(session,next_link):
    url = BASE_URL + next_link

    session.get(url)
    # 중간에 길이가 바뀌네 ,,,, ㅠ
    my_ip = ip

    i = 0
    while(len(my_ip) > i):
        my_ip = my_ip.replace(str(i),str(ord(str(i)[0])))
        i +=1

    my_ip = my_ip.replace('.','')
    my_ip = my_ip[0:10]
    answer = int(my_ip) *2
    answer = int(my_ip) /2
    answer = str(answer).replace(".","")
    answer
    flag_path  = url[:-11]+ '/answerip/{}_{}.php'.format(answer,my_ip)
    response = session.get(flag_path)

    print(response.text)

def main():
    session = requests.session()
    login(session)
    global ip
    ip = input("자신의 공인 IP 입력: ")
    next_link = solve_1(session)
    next_link = solve_2(session,next_link)
    next_link = solve_3(session,next_link)
    next_link = solve_4(session,next_link)
    next_link = solve_5(session,next_link)
    next_link = solve_6(session,next_link)
    next_link = solve_7(session,next_link)
    next_link = solve_8(session,next_link)
    next_link = solve_9(session,next_link)
    solve_10(session,next_link)

if __name__=='__main__':
    main()