import boto
import boto.s3.connection
access_key = 'UTS38U1T232ZK9UAE0CZ'
secret_key = '6g7d9NqUSJfipcOZTD7HAbJE9LBYjNLwpzXHbQOS'
import boto
import boto.s3.connection
import numpy as np

conn = boto.connect_s3(
aws_access_key_id = access_key,
aws_secret_access_key = secret_key,
host = '192.168.1.233',
port=7480,
is_secure=False,
calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)
# bucket = conn.create_bucket('my-new-bucket')
for bucket in conn.get_all_buckets():
        print "{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
)

import csv
import os
bucket = conn.get_bucket('meinian')
disk_path_N = "/home/zdy/python_script/meinian_data1228/"
#disk_path_P = "/home/zdy/python_script/meinian_data/P/"
series_uids = np.load('./series_70.npy').tolist()

temp_list = list()
#with open("./s3_temp1.csv", 'r') as ftp:
#    ftp_reader = csv.reader(ftp)
#    for row in ftp_reader:
#        temp_list.append(row[0])

with open('./MN-12-1-16-sp440.csv', 'r') as f:
    spamreader = csv.reader(f)
    title = spamreader.next()
    for row in spamreader:
        jianpei_flag = row[3]
        study_uid = row[1]
        series_uid = row[2]
        if series_uid in temp_list:
            continue
        if series_uid not in series_uids:
            continue
        rs = bucket.get_all_keys(prefix= study_uid + "/" + series_uid + "/")
        if not len(rs) > 0:
            continue
        dcm_path = os.path.join(disk_path_N, study_uid, series_uid)
        if not os.path.exists(dcm_path):
            os.makedirs(dcm_path)
        for key_object in rs:
            key = bucket.get_key(key_object.name)
            key.get_contents_to_filename(os.path.join(disk_path_N, key_object.name))
        #if jianpei_flag == 'P':
        #    dcm_path = os.path.join(disk_path_P, study_uid, series_uid)
        #    if not os.path.exists(dcm_path):
        #        os.makedirs(dcm_path)
        #    for key_object in rs:
        #        key = bucket.get_key(key_object.name)
        #        key.get_contents_to_filename(os.path.join(disk_path_P, key_object.name))
#        with open("./s3_temp1.csv", 'a') as ft:
#            tmp = csv.writer(ft)
#            tmp.writerow([series_uid])
        print "downloaded series is {}".format(series_uid)