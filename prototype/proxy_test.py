import requests
from spider import spider

def test():
    proxies = {
    'http': 'http://10.197.85.181:7890',
    'https': 'https://10.197.85.181:7890',
    }

    url = 'http://icanhazip.com'

    response1 = requests.post(url, proxies=proxies)
    response2 = requests.post(url)
    if(response1.text == response2.text):
        requests.post('https://api.day.app/dRRBWhzDHmBcfXwsj3QJPZ/Proxy_Failed/Please Change IP')
        raise ValueError("Proxy test Failed!")
    else:
        print("No error found in proxy")
    
    video = spider("http://api.bilibili.com/x/web-interface/view/detail?aid=170001",{})
    
    if video['code'] == -412:
        requests.post('https://api.day.app/dRRBWhzDHmBcfXwsj3QJPZ/CODE_412/Please Change IP')
        raise ValueError("CODE -412, Please Change IP")
    else:
        print("No code fount. Ready to go!")


