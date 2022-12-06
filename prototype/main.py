from MultiThreading import MultiThreading
import os
import time
import proxy_test

proxy_test.test()

## Use 170000 and 170100 when you test your code
start = 170250
end = 172000

cookies = {}
url_format = "https://api.bilibili.com/x/web-interface/view/detail?aid={}"

l = []

current_path = os.path.dirname(__file__)

filename = current_path + f'/data/{start}_to_{end}'

time_start = time.time()

pointer = start

step = 10

n = 0

while pointer + step <= end:

    MultiThreading(l,pointer,pointer+step-1,cookies,url_format,filename)

    # MultiThreading(start,end,cookies,url_format,filename)
    
    pointer = pointer + step
    
    n = n + 1
    
    if n*step % 1000 == 0:
        
        print(pointer)
        
    if n*step % 10000 == 0 and pointer < end:
        
        time.sleep(600)
    
    elif n*step % 2500 == 0 and pointer < end:
        
        time.sleep(180)
    
    else:
    
        time.sleep(2)
        
os.system(f'mkdir {current_path}/storage/data_{start}_{end} && mv {current_path}/data/* {current_path}/storage/data_{start}_{end}')


print("time use: "+ str(time.time() - time_start))

print("successfully get: "+str(len(l))+" videos")