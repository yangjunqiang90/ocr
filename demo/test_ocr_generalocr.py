#-*- coding: UTF-8 -*-
import sys
sys.path.append('../SDK')  
import optparse
import time
import apiutil
import base64
import json

app_key = 'H0WuXP3FsKVJfb3S'
app_id = '2128121458'

if __name__ == '__main__':
    #with open('../data/generalocr.jpg', 'rb') as bin_data:
    with open('../data/a.jpg', 'rb') as bin_data:
        image_data = bin_data.read()

    ai_obj = apiutil.AiPlat(app_id, app_key)

    print '----------------------SEND REQ----------------------'
    rsp = ai_obj.getOcrGeneralocr(image_data)

    k=0
    for i in rsp.values():
        k += 1
        print k,"\n"
        print  i

    if rsp['ret'] == 0:
        for i in rsp['data']['item_list']:
            print i['itemstring'] 
            #print i['itemcoord'] 
            #print i['words'] 
        print '----------------------API SUCC----------------------'
    else:
        print json.dumps(rsp, encoding="UTF-8", ensure_ascii=False, sort_keys=False, indent=4)
        print '----------------------API FAIL----------------------'
