from pa import pa
import os
import time
from build_database import build_database

start = 100000
end = 200000

cookies = {}
url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"

l = []

current_path = os.path.dirname(__file__)

filename = current_path+'/data/Test_Tags_10000_2.csv'

time_start=time.time()

pointer = start

step = 100

n = 0

while pointer + step <= end:

    pa(l,pointer,pointer+step-1,cookies,url_format,filename)

    # pa(start,end,cookies,url_format,filename)
    
    pointer = pointer + step
    
    n = n + 1
    
    if n*step % 100 == 0:
        
        print(pointer)
        
    if n*step % 2500 == 0 and pointer < end:
        
        time.slepp(1200)
    
    elif n*step % 2500 == 0 and pointer < end:
        
        time.sleep(500)
    
    else:
    
        time.sleep(10)

print("time use: "+ str(time.time() - time_start))

print("successfully get: "+str(len(l))+" videos")