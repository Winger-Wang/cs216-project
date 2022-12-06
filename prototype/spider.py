import requests

def spider(url,cookie = {}):

    proxies = {
    'http': 'http://10.197.85.181:7890',
    'https': 'https://10.197.85.181:7890',
    }
    
    if len(cookie) == 0:
    
        r = requests.get(url,proxies=proxies)
        
        # print(r)
    
    else:
        
        r = requests.get(url,cookies=cookie,proxies=proxies)
    
    return r.json()