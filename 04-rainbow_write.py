import hashlib
from tqdm import tqdm
import re

SALT = 'salt_for_you'
fd = open("rainbow.txt",'w')


def sha1_500(plain_text):
    for i in range(500):
        plain_text = hashlib.sha1(plain_text.encode("ascii")).hexdigest()
    return plain_text


def reduce_function(hash):
    '''
    축소 함수 : 추출된 해시 함수로부터 다음 평문을 만든다.
    로직 : 해시값에서 숫자 8자리 추출해서 다음 평문으로 만든다.
    '''
    numbers = re.findall("\d",hash)

    # 맨 앞에서 0이 연속으로 나온 경우 3가지만 제거해 준다.
    if (numbers[0] == '0'):
        if(numbers[1] == '0'):
            if(numbers[2] == '0'):
                numbers = numbers[3:]
            else:
                numbers = numbers[2:]
        else:
            numbers = numbers[1:]

    next_plain_number = ''
    # 해시 값에 숫자가 8개 이하로 존재할 수 있는 가능성 인지하고 처리 해줄 것
    for i in range(8):
        next_plain_number +=numbers[i]

    return int(next_plain_number)



# 하나의 해쉬체인은 100개로 한다.
def make_hash_chain(number):
    # 반환값은 [start,end] 로 한다.
    plain_number = number
    for i in range(100):
        hash_value = sha1_500(str(plain_number) + SALT)
        plain_number = reduce_function(hash_value)
#        print(hash_value)
#        print(plain_number)
    return hash_value




#def trace_hash_chain()

for number in tqdm(range(10000000,10100000)):
    try:
        hash_value = make_hash_chain(number)
        result =str(number) + ':' + str(hash_value) + '\n'
        fd.write(result)
    except:
        continue
