from spider import spider
from dic2csv import read_Tags
import threading

def build_database(l,i ,url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}",cookies = {}, filename = ""):
    
    
    lock = threading.Lock()
    
    with lock:
    
        video = spider(url_format.format(str(i)),cookies)
        
        # print(i)
        
        # print(video['code'])
            
            
        if(video['code'] == 0):
            
            data = video['data']
        
            read_Tags(l, data['Tags'], i , filename)
            
        # else:
            
            # print(video['code'])
                
    