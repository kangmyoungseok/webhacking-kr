import hashlib
from tqdm import tqdm

def sha1_500(plain_text):
    for i in range(500):
        plain_text = hashlib.sha1(plain_text.encode("ascii")).hexdigest()
    return plain_text

SALT = 'salt_for_you'   
fd = open("dictionary.txt",'w')


def reduce_function(encrypt_text):

for number in tqdm(range(10000000,20000000)):
    try:
        plain_text = str(number) + SALT
        hash_value = sha1_500(plain_text)
        result =str(number) + ':' + str(hash_value) + '\n'
        fd.write(result)
    except:
        fd.close()
