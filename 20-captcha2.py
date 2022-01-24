import requests
from bs4 import BeautifulSoup
LOGIN_FLAG = "<script>location.href='/';</script>"

def login(session):
    url = "https://webhacking.kr/login.php?login"
    id = str(input("webhacking.kr,id : "))
    pw = str(input("webhacking.kr,pw : "))   
    data = {'id' : id, 'pw' : pw}
    response = session.post(url,data=data)    
    if( LOGIN_FLAG in response.text ):
        print("login success, id : " + id)

def get_captcha(session):
    url = "https://webhacking.kr/challenge/code-4/"
    response = session.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    captcha = soup.select_one("body > form > table > tr:nth-child(3) > td:nth-child(2) > input:nth-child(2)").get_attribute_list('value')[0]
    return captcha

def send_captcha(session,captcha):
     url = "https://webhacking.kr/challenge/code-4/"
     data = {
         'id':'123',
         'cmt' : '1234',
         'captcha' : captcha
     }
     response = session.post(url,data=data)
     print(response.text)


def main():
    session =requests.session()
    login(session)
    captcha = get_captcha(session)
    send_captcha(session,captcha)
    
if __name__ == '__main__':
    main()