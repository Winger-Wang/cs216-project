import csv

def read_Tags(tags, i = 0, filename = "Tags.csv"):
    
    
    # print('reading tags')
    
    myFile = open(filename, 'w')

    writer = csv.writer(myFile)
    
    writer.writerow(['aid','tag_id', 'tag_name', 'cover','head_cover','content','short_content',
                 'type','state','ctime','count','is_atten','likes','hates','attribute',
                 'liked','hated','extra_attr','music_id','tag_type','is_activity','color',
                 'alpha','is_season','subscribed_count','archive_count','featured_count',
                 'jump_url'])
    
    for tag in tags:
    
        writer.writerow([i,tag.values()])
    
    myFile.close()
    
    # print('write success')