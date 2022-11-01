import threading
import build_database

def pa(start = 0, end = 0, cookies = [], url_format = "http://api.bilibili.com/x/web-interface/view/detail?aid={}" ):
    
    threads = []

    for i in range (start,end):
        
        threads.append(threading.Thread(target=build_database, args=(url_format.format(str(i)), cookies)))
        
    for thread in threads:
        
        thread.start()
        
    for thread in threads:
        
        thread.join()