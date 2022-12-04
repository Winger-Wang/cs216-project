# By Matty Huan

def read_hot_share(l, hotshares, i = 0, filename = "Hot_share.csv"):
    
    lock = threading.Lock()
    
    with lock:
        
        # print('reading tags')
        
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                for hotshare in hotshares:
                    
                    hotshare["aid"] = i
                
                    writer.writerow(hotshare.values())
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                ## Your main work is to change this part
                
                writer.writerow(['show','list','aid'])
                
                for hotshare in hotshares:
                    
                    hotshare["aid"] = i
                
                    writer.writerow(hotshare.values())
        
        l.append(i)