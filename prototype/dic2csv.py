import csv
import threading
import os

import collections ## for flatten()

"""
忽略所有list, 只保留dictionary并且完全展开的术式
贡献者: GNK48-Catears
"""

def flatten(d, parent_key='', sep='_'):
    type_list =type([]) # type of list, in a safe way
    items = []
    liststorage = [] # this variable don't work rn
    for k, v in d.items(): # two items, d is the first (keys) while v is the second (values)
        new_key = parent_key + sep + k if parent_key else k # if they receive parent key as input
        if isinstance(v, type_list):
            try:
                liststorage.append((new_key,v))
            except:
                print("Type 2:")
                print(v)
                print(new_key)
        elif isinstance(v, collections.MutableMapping):
            # try:

            items.extend(flatten(v, new_key, sep=sep).items()) # there will be a [0] in future
            # except:
            #     print("Type 1:")
            #     print(v)
            #     print(new_key)
                
                # return "Error occurs"

        else:
            try:
                items.append((new_key, v))
            except:
                print("Type 3:")
                print(v)
                print(new_key)
    return dict(items)#, dict(liststorage) # 未来还要自动return一个list，现在暂时不用


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
        
        # l.append(i)
        # print('write success')
        
## Please define your functions here, you can copy paste my function and adjust the content
"""
read View: the main function, make view .csv file and run the other two
read_View_pages: make page .csv file
read_View_honor: make honor_reply_honor .csv file
author: GNK48-Catears
"""

# def read_View_pages(View, fname, aid, parent_name):

#     filename = fname+'_pages.csv'

#     View_pages = View["pages"]

#     if ~(os.path.exists(filename)):

#         header = flatten(View_pages[0], parent_key=parent_name).copy()

#         header["aid"]=aid
        

#         F_header = open(filename,'w', encoding = "utf-8-sig", newline="")
#         writer = csv.writer(F_header)
#         ## make header
        
#         writer.writerow(header.keys())
#         F_header.close()

#     ## write rows

#     F_View_pages = open(filename, 'a', encoding = "utf-8-sig", newline="")
#     writer1 = csv.writer(F_View_pages)

#     for page in View_pages:
#         page0 = page.copy()
#         page0["aid"]=aid
#         page_f = flatten(page0)
#         writer1.writerow(page_f.values())

#     F_View_pages.close()

    # return "View_pages constructed" # humorous =)

def read_View_honors(View, fname, aid, parent_name): # can be chances that video come without honor at all
    
    filename = fname + '_honor_reply_honor.csv'
    View_honor = View["honor_reply"]["honor"]
    
    if os.path.exists(fname+'.csv'):

        F_View_honor = open(filename, 'a', encoding = "utf-8-sig", newline="")

        writer = csv.writer(F_View_honor)

        for honor in View_honor:

            honor0 = flatten(honor,parent_name)
            honor0["aid"]=aid
            # print(honor0.keys())
            # print(honor0.values())
            # honor_f = flatten(honor0)
            # honor_f["aid"]=aid
            writer.writerow(honor0.values())

        F_View_honor.close()

    else:

        F_View_honor = open(filename, 'w', encoding = "utf-8-sig", newline="")

        writer = csv.writer(F_View_honor)

        header = flatten(View_honor[0], parent_key=parent_name).copy()
        header["aid"]=aid

        writer.writerow(header.keys())

        for honor in View_honor:
            honor0 = flatten(honor,parent_name)
            honor0["aid"]=aid
            # print(honor0.keys())
            # print(honor0.values())
            # honor_f = flatten(honor0)
            # honor_f["aid"]=aid
            writer.writerow(honor0.values())

        F_View_honor.close()
    # return "View_honors collected"



def read_View(l, View, aid = 0, filename = "View"):
    
    lock = threading.Lock()

    
    with lock:
        flatview = flatten(View,'View')
        flatview["aid"]=aid

        if os.path.exists(filename+'.csv'):

            ViewFile = open(filename+'.csv', 'a',encoding = "utf-8-sig", newline="")
            vwriter = csv.writer(ViewFile)
            # vwriter.writerow(flatview.keys())
            vwriter.writerow(flatview.values())
            ViewFile.close()
        
        else:
            ViewFile = open(filename+'.csv', 'w',encoding = "utf-8-sig", newline="")
            vwriter = csv.writer(ViewFile)
            # vwriter.writerow(flatview.keys())
            vwriter.writerow(flatview.values())
            ViewFile.close()
        # read_View_pages(View, filename,aid, 'View_pages' )
        try:
            read_View_honors(View, filename, aid, 'View_honor_reply_honor')
        except:
            print("no honor found")
        
        # read_View_pages(View, filename, aid, "View_pages")

    return "View Successful"


"""
read_Card: read everything in Card group, no list pure fun
author: GNK48-Catears
"""
def read_Card(l, Card, aid = 0, filename = "Card",parent_name = "Card"):
    lock = threading.Lock()

    flatCard = flatten(Card, parent_key=parent_name)

    flatCard["aid"] = aid

    if os.path.exists(filename+'.csv'):

        F_Card = open(filename+'.csv', 'a', encoding = "utf-8-sig", newline="")

        writer = csv.writer(F_Card)
        writer.writerow(flatCard.values())

        F_Card.close()

    
    else:

        F_Card = open(filename+'.csv', 'w', encoding = "utf-8-sig", newline="")

        writer = csv.writer(F_Card)

        writer.writerow(flatCard.keys())

        writer.writerow(flatCard.values())

        F_Card.close()

    return "Read Successful"