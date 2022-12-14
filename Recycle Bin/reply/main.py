from pa import pa
import os
import time
from build_database import build_database

## Use 170000 and 170100 when you test your code
start = 170000
end = 170100

cookies = {}
url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"

l = []

current_path = os.path.dirname(__file__)

filename = current_path+'/data/Test_Eric_'

time_start=time.time()

pointer = start

step = 100

n = 0

while pointer + step <= end:

    pa(l,pointer,pointer+step-1,cookies,url_format,filename)

    # pa(start,end,cookies,url_format,filename)
    
    pointer = pointer + step
    
    n = n + 1
    
    if n*step % 1000 == 0:
        
        print(pointer)
        
    if n*step % 10000 == 0 and pointer < end:
        
        time.sleep(1200)
    
    elif n*step % 2500 == 0 and pointer < end:
        
        time.sleep(500)
    
    else:
    
        time.sleep(10)

print("time use: "+ str(time.time() - time_start))

print("successfully get: "+str(len(l))+" videos")