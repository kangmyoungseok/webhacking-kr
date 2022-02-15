from hashlib import md5
from tqdm import tqdm
from colorama import Fore

for i in range(1000000000):
    raw_md5 = md5(str(i).encode("ascii")).digest()
    if(b'\x27\x3d\x27' in raw_md5):
        print(Fore.GREEN + '[+] ' + str(i) +' : ' + str(raw_md5))
        
    
    