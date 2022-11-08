import csv
import threading
import os

def read_Tags(l, tags, i = 0, filename = "Tags.csv"):
    
    lock = threading.Lock()
    
    with lock:
        
        # print('reading tags')
        
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                for tag in tags:
                    
                    tag["aid"] = i
                
                    writer.writerow(tag.values())
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                ## Your main work is to change this part
                
                writer.writerow(['tag_id', 'tag_name', 'cover','head_cover','content','short_content',
                            'type','state','ctime','count','is_atten','likes','hates','attribute',
                            'liked','hated','extra_attr','music_id','tag_type','is_activity','color',
                            'alpha','is_season','subscribed_count','archive_count','featured_count',
                            'jump_url','aid'])
                
                for tag in tags:
                    
                    tag["aid"] = i
                
                    writer.writerow(tag.values())
        
        l.append(i)
        # print('write success')
        
## Please define your functions here, you can copy paste my function and adjust the content