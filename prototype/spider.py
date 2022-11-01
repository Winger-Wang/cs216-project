import requests

def spider (url,cookie = []):
    
    if len(cookie) == 0:
    
        r = requests.get(url)
    
    else:
        
        r = requests.get(url,cookies=cookie)
    
    return r