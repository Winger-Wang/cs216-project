from pa import pa
import os
import time

start = 170000
end = 180000

cookies = {}
url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"

l = []

current_path = os.path.dirname(__file__)

filename = current_path+'/data/Test_Tags_10000.csv'

time_start=time.time()

pointer = start

step = 50

n = 0

while pointer + step <= end:

    pa(l,pointer,pointer+step-1,cookies,url_format,filename)

    # pa(start,end,cookies,url_format,filename)
    
    pointer = pointer + step
    
    n = n + 1
    
    if n*step % 100 == 0:
        
        print(pointer)
    
    if n*step % 5000 == 0:
        
        time.sleep(600)
    
    else:
    
        time.sleep(10)

print("time use: "+ str(time.time() - time_start))

print("successfully get: "+str(len(l))+" videos")