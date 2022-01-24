import base64
from urllib import parse

name = 'myoungseok'          # 1. 문자열
name_bytes = name .encode('ascii')  # 2. bytes형 변환
name_base64 = base64.b64encode(name_bytes)  #3. base64인코딩
name_base64_str = name_base64.decode('ascii')   # 결과값 문자열로 만들기

print(name)
print(name_bytes)
print(name_base64)
print(name_base64_str)



# 문제 풀이
# 1. guest를 문제에 따라서 20번 인코딩 후, 문자열 치환
result ='''Vm0wd%40QyUXlVWGxWV0d%5EV%21YwZDRWMVl%24WkRSV0%21WbDNXa%21JTVjAxV%40JETlhhMUpUVmpBeFYySkVUbGhoTVVwVVZtcEJlRll%26U%40tWVWJHaG9UVlZ%24VlZadGNFSmxSbGw%21VTJ0V%21ZXSkhhRzlVVmxaM%21ZsWmFjVkZ0UmxSTmJFcEpWbTEwYTFkSFNrZGpSVGxhVmpOU%21IxcFZXbUZrUjA%21R%21UyMTRVMkpIZHpGV%21ZFb%24dWakZhV0ZOcmFHaFNlbXhXVm%21wT%21QwMHhjRlpYYlVaclVqQTFSMXBGV%40xOVWJGcFlaSHBHVjFaRmIzZFdha%21poVjBaT%40NtRkhhRk%26sYlhoWFZtMHhORmxWTUhoWGJrNVlZbFZhY%40xWcVFURlNNVlY%21VFZSU%21ZrMXJjRWxhU0hCSFZqRmFSbUl%2AWkZkaGExcG9WakJhVDJOdFJraGhSazVzWWxob%21dGWnRNWGRVTVZGM%21RVaG9hbEpzY0ZsWmJGWmhZMnhXY%21ZGVVJsTk%26WbFkxVkZaU%21UxWnJNWEpqUld%5EaFUwaENTRlpxUm%21GU%40JVbDZXa%21prYUdFeGNHOVdha0poVkRKT%40RGSnJhR%40hTYXpWeldXeG9iMWRHV%40%26STldHUlZUVlpHTTFSVmFHOWhiRXB%2AWTBac%21dtSkdXbWhaTVZwaFpFZFNTRkpyTlZOaVJtOTNWMnhXYjJFeFdYZE%26WVlpUWVRGd%21YxbHJXa%24RUUmxweFVtMUdVMkpWYkRaWGExcHJZVWRGZUdOSE9WZGhhMHBvVmtSS%21QyUkdTbkpoUjJoVFlYcFdlbGRYZUc%26aU%21XUkhWMjVTVGxOSGFGQlZiVEUwVmpGU%21ZtRkhPVmhTTUhCNVZHeGFjMWR0U%40tkWGJXaGFUVzVvV0ZreFdrZFdWa%24B%2AVkdzMVYwMVZiekZXYlhCS%21RWZEZlRmRZWkU%21V%21ZscFVXV%24RrVTFsV%21VsWlhiVVpPVFZad%40VGVXlkREJXTVZweVkwWndXR0V%5EY0ROV%40FrWkxWakpPU%21dKR%21pGZFNWWEJ%40Vm%210U%21MxUXlUWGxVYTFwb%21VqTkNWRmxZY0ZkWFZscFlZMFU%21YVUxcmJEUldNalZUVkd%5Ea%21NGVnNXbFZXYkhCWVZHdGFWbVZIUmtoUFYyaHBVbGhDTmxkVVFtRmpNV%21IwVTJ0a%21dHSlhhR0ZVVnpWdlYwWnJlRmRyWkZkV%40EzQjZWa%40R%2ATVZkR%21NsWmpSV%24hYWWxoQ%21RGUnJXbEpsUm%21SellVWlNhRTFzU%40%26oV%21Z%2AQjRUa%40RHUjFaWVpHaFNWVFZWVlcxNGQyVkdWblJOVldSV%21RXdHdWMWxyVW%21GWFIwVjRZMGhLV%40xaWFVrZGFWV%21JQVTBVNVYxcEhhR%40hOU0VKMlZtMTBVMU%21%5EVVhsVmEyUlZZbXR%24YUZWdGVFdGpSbHB%5EVkcwNVYxWnNjRWhYVkU%21dllWVXhXRlZ%21Y0ZkTlYyaDJWMVphUzFJeFRuVlJiRlpYVFRGS0%26sWkdVa%40RWTVZwMFVtdG9VRlp0YUZSVVZXaERVMnhhYzFwRVVtcE%26WMUl%24VlRKMGExZEhTbGhoUjBaVlZucFdkbFl%24V%40%26KbFJtUnlXa%21prVjJFelFqWldhMlI%40VFZaWmVWTnJaR%40hOTW%21oWVdWUkdkMkZHV%40xWU%40JGcHNVbTFTTVZVeWN%2ARlhSa%24BaVVc%21b%21YxWXphSEpVYTJSSFVqRmFXVnBIYUZOV%21ZGWldWbGN%5ETkdReVZrZFdXR%24hyVWpCYWNGVnRlSGRsYkZsNVpVaGtXRkl%24VmpSWk%21GSlBWMjFGZVZWclpHRldNMmhJV%21RJeFMxSXhjRWhpUm%21oVFZsaENTMVp0TVRCVk%21VMTRWbGhvV0ZkSGFGbFpiWGhoVm%21%5Ec%40NscEhPV%24BTYkhCNFZrY%24dOVll%5EV%40%26OalJXaFlWa%21UxZGxsV%21ZYaFhSbFp%26WVVaa%21RtRnNXbFZXYTJRMFdWWktjMVJ%21VG%21oU%40JGcFlXV%24hhUm%21ReFduRlJiVVphVm0xU%21NWWlhkRzloTVVwMFlVWlNWVlpXY0dGVVZscGhZekZ%24UlZWdGNFNVdNVWwzVmxSS0%21HRXhaRWhUYkdob%21VqQmFWbFp0ZUhkTk%21WcHlWMjFHYWxacmNEQmFSV%21F%24VmpKS%40NsTnJhRmRTTTJob%21ZrUktSMVl%5EVG%26WVmJFSlhVbFJXV%21ZaR%21l%2ARmlNV%21JIWWtaV%21VsZEhhRlJVVm%21SVFpXeHNWbGRzVG%21oU%21ZFWjZWVEkxYjFZeFdYcFZiR%40hZVm%21%5Ed%21lWcFZXbXRrVmtwelZtMXNWMUl%2AYURWV0%21XUXdXVmRSZVZaclpGZGliRXB%26Vld0V%21MySXhiRmxqUldSc%21ZteEtlbFp0TURWWFIwcEhZMFpvV%40sxSGFFeFdNbmhoVjBaV%40NscEhSbGROTW%21oSlYxUkplRk%21%5EU%21hoalJXUmhVbXMxV0ZZd%21ZrdE%26iRnAwWTBWa%21dsWXdWalJXYkdodlYwWmtTR0ZHV%40xwaVdHaG9WbTE0YzJOc%21pISmtSM0JUWWtad0%26GWlhNVEJOUmxsNFYyNU9hbEpYYUZoV%40FrNVRWRVpzVlZGWWFGTldhM0I%40VmtkNFlWVXlTa%21pYV0hCWFZsWndSMVF%5EV%40tOVmJFSlZUVVF%24UFE9PQ%3D%3D'''
string = 'guest'
string_bytes = string.encode('ascii')
string_base64 = string_bytes

for i in range(20):
    string_base64 = base64.b64encode(string_base64)

string_base64_20_str = string_base64.decode('ascii')

replace_str = string_base64_20_str
replace_str = replace_str.replace("1","!")
replace_str = replace_str.replace("2","@")
replace_str = replace_str.replace("3","$")
replace_str = replace_str.replace("4","^")
replace_str = replace_str.replace("5","&")
replace_str = replace_str.replace("6","*")
replace_str = replace_str.replace("7","(")
replace_str = replace_str.replace("8",")")

replace_str_url_encode = parse.quote(replace_str)

if(replace_str_url_encode == result):
    print("쿠키 값과 내가 인코딩 한 값이 동일")
else:
    print("쿠키 값과 내가 인코딩 한 값이 다름")


# 디코딩
# 위에서 인코딩한 내용을 디코딩 한다.
## 치환 -> 디코딩 
## 디코딩 해야 할 문자열 : replace_str

### 치환
replace_str = replace_str.replace("!","1")
replace_str = replace_str.replace("@","2")
replace_str = replace_str.replace("$","3")
replace_str = replace_str.replace("^","4")
replace_str = replace_str.replace("&","5")
replace_str = replace_str.replace("*","6")
replace_str = replace_str.replace("(","7")
replace_str = replace_str.replace(")","8")

replace_str_bytes = replace_str.encode("ascii")

### base64 디코딩 20번
replace_str_64decoded = replace_str_bytes
for i in range(20):
    replace_str_64decoded = base64.b64decode(replace_str_64decoded)

decoded_str = replace_str_64decoded.decode("ascii")




def base64_encode_20(string):
    string_bytes = string.encode('ascii')
    string_base64 = string_bytes

    for i in range(20):
        string_base64 = base64.b64encode(string_base64)
        #print(string_base64)

    string_base64_20_str = string_base64.decode('ascii')

    replace_str = string_base64_20_str
    replace_str = replace_str.replace("1","!")
    replace_str = replace_str.replace("2","@")
    replace_str = replace_str.replace("3","$")
    replace_str = replace_str.replace("4","^")
    replace_str = replace_str.replace("5","&")
    replace_str = replace_str.replace("6","*")
    replace_str = replace_str.replace("7","(")
    replace_str = replace_str.replace("8",")")

    return replace_str

base64_encode_20("admin")
base64_encode_20("nimda")