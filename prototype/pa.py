import threading
from build_database import build_database

def pa(l,start = 0, end = 0, cookies = {}, url_format = "", filename = ""):
    
    threads = []
    
    for i in range (start,end):
        
        threads.append(threading.Thread(target=build_database, args=(l, i,url_format, cookies, filename)))
        
    for thread in threads:
        
        thread.start()
        
    for thread in threads:
        
        thread.join()