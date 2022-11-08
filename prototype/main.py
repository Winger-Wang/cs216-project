from pa import pa
import os
import time

start = 170000
end = 172000

cookies = {}
url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"

l = []

current_path = os.path.dirname(__file__)

filename = current_path+'/data/Test_Tags_2000.csv'

time_start=time.time()

pointer = start

step = 50

while pointer + step <= end:

    pa(l,pointer,pointer+step-1,cookies,url_format,filename)

    # pa(start,end,cookies,url_format,filename)
    
    pointer = pointer + step
    
    print(pointer)
    
    time.sleep(10)

print("time use: "+ str(time.time() - time_start))

print("successfully get: "+str(len(l))+" videos")