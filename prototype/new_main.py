from MultiThreading import MultiThreading
import os
import time
import proxy_test
import requests



all_start = 1200000

url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"
cookies = {}

current_path = os.path.dirname(__file__)

step_large = 10000

n = 0

while(all_start + n * step_large <= 2000000):

    proxy_test.test()

    start = all_start + n * step_large
    end = all_start + (n+1) * step_large

    n += 1

    l = []

    filename = current_path + f'/data/{start}_to_{end}'

    time_start = time.time()

    pointer = start

    step = 10

    while pointer + step <= end:
        
        MultiThreading(l,pointer,pointer+step-1,cookies,url_format,filename)


        if (pointer - start) % 1000 == 0:

            print(pointer)
            time.sleep(30)
            print("slept 30")
            requests.post(f'https://api.day.app/dRRBWhzDHmBcfXwsj3QJPZ/Succeed/{pointer}')

        else:

            time.sleep(2)

        pointer = pointer + step
    
    os.system(f'mkdir {current_path}/storage/data_{start}_{end} && mv {current_path}/data/* {current_path}/storage/data_{start}_{end}')
    
    print("time use: "+ str(time.time() - time_start))

    print("successfully get: "+str(len(l))+" videos")

    print("sleep 300")
    time.sleep(300)
    print("slept 300")



        










