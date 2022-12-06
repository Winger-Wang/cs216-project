import csv
import threading
import os
import collections ## for flatten()

def flatten(d, parent_key='', sep='_'):
    # """
    # 忽略所有list, 只保留dictionary并且完全展开的术式
    # 贡献者: GNK48-Catears
    # """
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
        elif isinstance(v, collections.abc.MutableMapping):
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



#### read_Tage by Ian#####
def read_Tags(l, tags, i = 0, filename = "Tags.csv"):
    
    lock = threading.Lock()
    
    row = ['tag_id', 'tag_name', 'cover','head_cover','content','short_content',
            'type','state','ctime','count','is_atten','likes','hates','attribute',
            'liked','hated','extra_attr','music_id','tag_type','is_activity','color',
            'alpha','is_season','subscribed_count','archive_count','featured_count',
            'jump_url','aid']
    
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
                
                writer.writerow(row)
                
                for tag in tags:
                    
                    tag["aid"] = i
                
                    writer.writerow(tag.values())

        # print('write success')

#### read_View by Jerry#####
def read_View(l, View, aid = 0, filename = "View"):
    # """
    # read View: the main function, make view .csv file and run the other two
    # read_View_pages: make page .csv file
    # read_View_honor: make honor_reply_honor .csv file
    # author: GNK48-Catears
    # """
    
    lock = threading.Lock()

    
    with lock:
        flatview = flatten(View,'View')
        flatview["aid"]=aid

        if os.path.exists(filename):

            ViewFile = open(filename, 'a',encoding = "utf-8-sig", newline="")
            vwriter = csv.writer(ViewFile)
            # vwriter.writerow(flatview.keys())
            vwriter.writerow(flatview.values())
            ViewFile.close()
        
        else:
            ViewFile = open(filename, 'w',encoding = "utf-8-sig", newline="")
            vwriter = csv.writer(ViewFile)
            # vwriter.writerow(flatview.keys())
            vwriter.writerow(flatview.values())
            ViewFile.close()
        # read_View_pages(View, filename,aid, 'View_pages' )
        try:
            read_View_honors(View, filename, aid, 'View_honor_reply_honor')
        except:
            # print(f"{aid} no honor found")
            ...
        
        read_View_pages(View, filename, aid, "View_pages")

    return "View Successful"

def read_View_pages(View, fname, aid, parent_name):

    filename = fname[:-4]+'_pages.csv'

    View_pages = View["pages"]
    
    header = flatten(View_pages[0], parent_key=parent_name).copy()

    header["aid"]=aid

    if (os.path.exists(filename)):
        F_View_pages = open(filename, 'a', encoding = "utf-8-sig", newline="")
        writer1 = csv.writer(F_View_pages)

        for page in View_pages:
            page0 = page.copy()
            page0["aid"]=aid
            page_f = flatten(page0)
            writer1.writerow(page_f.values())
            
            if len(page_f.values()) != len(header):
            
                raise ValueError("Error in Read_View_pages")

        F_View_pages.close()

    else:
    

        F_header = open(filename,'w', encoding = "utf-8-sig", newline="")
        writer = csv.writer(F_header)
        ## make header
        
        writer.writerow(header.keys())
        

        for page in View_pages:
            page0 = page.copy()
            page0["aid"]=aid
            page_f = flatten(page0)
            writer.writerow(page_f.values())
            
            if len(page_f.values()) != len(header):
                
                raise ValueError("Error in Read_View_pages")

        F_header.close()

    ## write rows

    # return "View_pages constructed" # humorous =)

def read_View_honors(View, fname, aid, parent_name): # can be chances that video come without honor at all
    
    filename = fname[:-4] + '_honor_reply_honor.csv'
    View_honor = View["honor_reply"]["honor"]
    
    header = flatten(View_honor[0], parent_key=parent_name).copy()
    header["aid"]=aid
    
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
            
            if len(honor0.values()) != len(header):
                
                raise ValueError("Error in Read]_View_honors")

        F_View_honor.close()

    else:

        F_View_honor = open(filename, 'w', encoding = "utf-8-sig", newline="")

        writer = csv.writer(F_View_honor)

        writer.writerow(header.keys())

        for honor in View_honor:
            honor0 = flatten(honor,parent_name)
            honor0["aid"]=aid
            # print(honor0.keys())
            # print(honor0.values())
            # honor_f = flatten(honor0)
            # honor_f["aid"]=aid
            writer.writerow(honor0.values())
            
            if len(honor0.values()) != len(header):
                    
                raise ValueError("Error in Read]_View_honors")

        F_View_honor.close()
    # return "View_honors collected"

#### read_Card by Jerry#####
def read_Card(l, Card, aid = 0, filename = "Card",parent_name = "Card"):
    # read_Card: read everything in Card group, no list pure fun
    # author: GNK48-Catears
    lock = threading.Lock()

    flatCard = flatten(Card, parent_key=parent_name)

    flatCard["aid"] = aid
    
    header = flatCard.keys()

    if os.path.exists(filename):

        F_Card = open(filename, 'a', encoding = "utf-8-sig", newline="")

        writer = csv.writer(F_Card)
        writer.writerow(flatCard.values())

        F_Card.close()
        
        if len(flatCard.values()) != len(header):
                
            raise ValueError("Error in Read_Card")        

    
    else:

        F_Card = open(filename, 'w', encoding = "utf-8-sig", newline="")

        writer = csv.writer(F_Card)

        writer.writerow(header)

        writer.writerow(flatCard.values())
        
        if len(flatCard.values()) != len(header):
                    
            raise ValueError("Error in Read_Card")

        F_Card.close()

    return "Read Successful"


### read_Related by Matty#####
def read_Related(l, relateds, i = 0, filename = "Related.csv"):
    
    lock = threading.Lock()
    
    # header = ['video','tid','tname','copyright','pic',
    #             'title','pubdate','ctime','desc','state','duration','rights',
    #             'owner','stat','dynamic','cid','dimension','short_link',
    #             'short_link_v2','up_from_v2','bvid','season_type','is_ogv',
    #             'ogv_info','rcmd_reason','aid']

    header = ['related_video','aid']

    # os.system("pause")

    with lock:
                
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                for related in relateds:
                    
                    tmp = {}
                    tmp["related_video"] = related["aid"]
                    tmp["aid"] = i

                    # related["from_aid"] = i
                
                    writer.writerow(tmp.values())
                    
                    # if len(related.values()) != len(header):
                        
                    #     raise ValueError("Error in Read_Related")
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                                
                writer.writerow(header)
                
                for related in relateds:

                    # print(related)
                    # print(related.type)
                    
                    tmp = {}
                    tmp["related_video"] = related["aid"]
                    tmp["aid"] = i

                    # related["from_aid"] = i
                
                    writer.writerow(tmp.values())
                    
                

#### read_Reply by Eric#####
def read_Reply(l,Reply,i=0,filename=""):
    if Reply == None:
        return
    else:
        read_Reply_main(l,Reply['page'],i,filename)
        read_Reply_replies(l,Reply['replies'],i,filename)

def read_Reply_main(l, Reply, i=0, filename="Reply_main.csv"):

    lock = threading.Lock()
    
    header = ["account", "count", "num", "size", "aid"]
    
    with lock:
        
        # print('reading tags')

        filename = filename[:-4] + "_main.csv"
        
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)

                Reply["aid"]=i
                
                writer.writerow(Reply.values())
                
                if len(Reply.values()) != len(header):
                        
                    raise ValueError("Error in Read_Reply_main")
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                ## Your main work is to change this part
                
                writer.writerow(header)

                Reply["aid"]=i

                writer.writerow(Reply.values())
                
                if len(Reply.values()) != len(header):
                            
                    raise ValueError("Error in Read_Reply_main")
                
                
def read_Reply_replies(l, Reply, i=0, filename="Reply_replies.csv"):
    lock = threading.Lock()
    
    if Reply == None:
        return
    else:
        Reply[0]['aid'] = i
    
    header = Reply[0].keys()
    
    with lock:
        
        # print('reading tags')

        filename= filename[:-4] + "_replies.csv"
        
        if os.path.exists(filename):
            
            with open(filename, 'a', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)


                
                for items in Reply:

                    items["aid"]=i
                    writer.writerow(items.values())
                    
                    if len(items.values()) != len(header):
                                
                        raise ValueError("Error in Read_Reply_replies")
            
        else:
        
            with open(filename, 'w', encoding = "utf-8-sig", newline="") as myFile:

                writer = csv.writer(myFile)
                
                ## Your main work is to change this part
                
                for items in Reply:

                    items["aid"]=i
                
                writer.writerow(header)
                
                for items in Reply:
                    writer.writerow(items.values())
                    
                    if len(items.values()) != len(header):
                                
                        raise ValueError("Error in Read_Reply_replies")
