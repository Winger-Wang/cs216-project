from MultiThreading import MultiThreading
import os
import time
import proxy_test



all_start = 1000000

url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"
cookies = {}

current_path = os.path.dirname(__file__)

step_large = 10000

n = 0

while(all_start + n * step_large < 2000000):

    proxy_test.test()

    n += 1

    start = all_start + n * step_large
    end = all_start + (n+1) * step_large

    l = []

    filename = current_path + f'/data/{start}_to_{end}'

    time_start = time.time()

    pointer = start

    step = 10

    while pointer + step <= end:
        
        MultiThreading(l,pointer,pointer+step-1,cookies,url_format,filename)

        pointer = pointer + step

        if pointer - start % 1000 == 0:

            print(pointer)

            time.sleep(30)

        else:

            time.sleep(2)
    
    os.system(f'mkdir {current_path}/storage/data_{start}_{end} && mv {current_path}/data/* {current_path}/storage/data_{start}_{end}')
    
    print("time use: "+ str(time.time() - time_start))

    print("successfully get: "+str(len(l))+" videos")

    time.sleep(300)



        









