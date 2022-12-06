import requests

def test():
    proxies = {
    'http': 'http://10.197.85.181:7890',
    'https': 'https://10.197.85.181:7890',
    }

    url = 'http://icanhazip.com'

    response1 = requests.post(url, proxies=proxies)
    response2 = requests.post(url)
    if(response1.text == response2.text):
        raise ValueError("Proxy test Failed!")
    else:
        print("No error found in proxy")


