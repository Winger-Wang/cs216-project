from spider import spider
from dic2csv import *
import threading

def build_database(l,i ,url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}",cookies = {}, filename = ""):
      
    lock = threading.Lock()
    
    with lock:
    
        video = spider(url_format.format(str(i)),cookies)
        
        # print(i)
        
        # print(video['code'])
            
            
        if(video['code'] == 0):
            
            data = video['data']
        
            read_Tags(l, data['Tags'], i , filename+"_TAG.csv")
            
            ## Please put your functions here and don't fogret to add "_xxx.csv" at the end of filename
            
        elif (video['code'] == -412):
            
            print(i)
            
            raise ValueError("CODE -412")
        
            
                
    