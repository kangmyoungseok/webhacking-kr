from hashlib import md5
import base64
hash_result = ''

for character in 'admin':
    enc = md5()
    enc.update(character.encode("ascii"))
    hash_value = enc.hexdigest()
    hash_result +=hash_value

hash_result_base64 = base64.b64encode(hash_result.encode("ascii"))

print(hash_result_base64)
