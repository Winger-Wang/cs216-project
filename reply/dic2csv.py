import csv
import threading
import os

def read_Reply(l,Reply,i=0,filename=""):
    read_Reply_main(l,Reply['page'],i,filename)
    read_Reply_replies(l,Reply['replies'],i,filename)

def read_Reply_main(l, Reply, i=0, filename="Reply_main.csv"):
    lock = threading.Lock()
    
    with lock:
        
        # print('reading tags')

        filename= filename + "Reply_main.csv"
        
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)

                Reply["aid"]=i
                
                writer.writerow(Reply.values())
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                ## Your main work is to change this part
                
                writer.writerow(["account", "count", "num", "size"])

                Reply["aid"]=i

                writer.writerow(Reply.values())
        l.append(i)
                
def read_Reply_replies(l, Reply, i=0, filename="Reply_replies.csv"):
    lock = threading.Lock()
    
    with lock:
        
        # print('reading tags')

        filename= filename + "Reply_replies.csv"
        
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)


                
                for items in Reply:

                    items["aid"]=i
                    writer.writerow(items.values())
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                ## Your main work is to change this part
                
                for items in Reply:

                    items["aid"]=i
                
                writer.writerow(Reply[0].keys())
                
                for items in Reply:
                    writer.writerow(items.values())

    



        

        #print('write success')
        
## Please define your functions here, you can copy paste my function and adjust the content