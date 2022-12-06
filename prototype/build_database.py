from spider import spider
from dic2csv import *
import threading
import os

def build_database(l ,i ,url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}",cookies = {}, filename = ""):
      
    lock = threading.Lock()

    l.append(i)
    
    with lock:
    
        video = spider(url_format.format(str(i)),cookies)
        
        # print(i)
        
        # print(video['code'])
            
            
        if(video['code'] == 0):

            # l.append[i]
            
            data = video['data']

            print(f'Parsing Number {i}')

            read_View(l, data['View'], i , filename+"_View.csv")

            read_Card(l, data['Card'], i , filename+"_Card.csv")
        
            read_Tags(l, data['Tags'], i , filename+"_Tags.csv")

            read_Reply(l, data['Reply'], i , filename+"_Reply.csv")

            read_Related(l, data['Related'], i , filename+"_Related.csv")
                                    
        elif (video['code'] == -412):
            
            print(i)
            
            raise ValueError("CODE -412")
        
            
                
    