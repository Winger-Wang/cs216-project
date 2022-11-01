from pa import pa
import os
import time

start = 170000
end = 170200

cookies = []
url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"

current_path = os.path.dirname(__file__)

filename = current_path+'\\data\\Test_Tags.csv'

time_start=time.time()

pa(start,end,cookies,url_format,filename)

print("time use: "+ str(time.time() - time_start))