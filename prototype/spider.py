import requests

def spider (url,cookie = []):
    
    if len(cookie) == 0:
    
        r = requests.get(url)
        
        # print(r)
    
    else:
        
        r = requests.get(url,cookies=cookie)
    
    return r.json()