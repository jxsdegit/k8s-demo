import pandas as pd
import os
import pymongo
import csv,re

#client = pymongo.MongoClient("mongodb://192.168.1.174:27019/")
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['diagnosis']
col = db['result_collection']

ll = []

#series_uids = pd.read_csv("F:\results(1).csv")['series_uid']
series_uids = ['1.3.12.2.1107.5.1.4.54893.30000017080100075515600010144']
print(series_uids)
for i in series_uids:
    myquery = {"image_uid": i}
    mydoc = col.find(myquery).sort([('timestamp', -1)])
    count = 0
    for d in mydoc:
        count + 1
        if count > 1:
            continue
        classfilys = d['sub_results']
        classfily = list(filter(lambda x: x['key']=='nodule', classfilys))
        if not classfily:
            continue
        classfily = classfily[0]
        focus = classfily['sub_results']
        for f in focus:
            #print(i, f['center'], f['confidence'])
            centers = f['center']
            confidences = f['confidence']
            ll.append((i,centers,confidences))
            print(ll)
        name=['one','two','three']
        test=pd.DataFrame(columns=name,data=ll)
        test.to_csv('F:\\results2.csv',encoding='utf-8')
