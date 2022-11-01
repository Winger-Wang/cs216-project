from pa import pa
import os
import time

start = 170000
end = 172000

current_path = os.path.dirname(__file__)

cookies = []
url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}"
filename = current_path+'\\data\\Tags_Test.csv'

time_start=time.time()

pa(start,end,cookies,url_format,filename)

print("time use: "+ str(time.time() - time_start))