import csv
import threading
import os

def read_Addits(l, view_addit, i = 0, filename = "view_addits.csv"):
    
    lock = threading.Lock()
    
    with lock:
        
        # print('reading tags')
        
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                    
                view_addit["aid"] = i
                
                writer.writerow(view_addit.values())
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                ## Your main work is to change this part
                
                writer.writerow(["63","64","69","71","72","aid"])
                
                    
                view_addit["aid"] = i
                
                writer.writerow(view_addit.values())
        
        l.append(i)
        # print('write success')
        
## Please define your functions here, you can copy paste my function and adjust the content