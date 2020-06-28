import os
import csv
import json
from glob import glob
from datetime import datetime
import time

def time_format(t):
    if isinstance(t, datetime):
        return t.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(t, float):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
    return t

study_uids = []
over_uids = []
datetime_range = ['2018-12-08', '2018-12-09', '2018-12-10', '2018-12-11', '2018-12-12']
for dr in datetime_range:
    file_list = glob("/mnt/cephfs_ssd/trace_out/study_json/{}/*.json".format(dr))
    for f in file_list:
        file_time = time_format(os.path.getctime(f))[:10]
        #if file_time in ["2018-12-01", "2018-12-02"]:
        with open(f, 'r') as fj:
            report = json.loads(fj.read())
            if report['negativePositive'] == 'O':
                study_uids.append(report["studyInstanceUID"])
            else:
                study_uid = report["studyInstanceUID"]
                over_uids.append(study_uid)
print len(study_uids)
print len(over_uids)