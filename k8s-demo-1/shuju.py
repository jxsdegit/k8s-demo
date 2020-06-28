import numpy as np
import pandas as pd
from glob import glob
import os


if __name__ == '__main__':
    src_base_path = ["/mnt/data/", "/mnt/cephfs_ssd/"]
    dst_path = '/media/usb/meinian_cache_dr/'
    #if not os.path.exists(dst_path):
    #    os.makedirs(dst_path)

    #study_uids = pd.read_excel("./report_export/csv/report_198118.csv").values[:,3]
    #study_uids = pd.read_excel("./csv/report198118-0705-0708.xlsx").values[:,2]
    #study_uids = pd.read_excel("./csv/MN197665_total_new.xlsx").values[:,3]
    study_uids = pd.read_csv("./meinian12_11-12_25.csv")['study_uid']
    print(len(study_uids))
    count = 0
    for study_uid in study_uids:
        study_uid_path_data = os.path.join(src_base_path[0], study_uid)
        study_uid_path_ceph = os.path.join(src_base_path[1], study_uid)
        src_path = None
        if os.path.exists(study_uid_path_data):
            src_path = study_uid_path_data
        if os.path.exists(study_uid_path_ceph):
            src_path = study_uid_path_ceph
        if not src_path:
            continue

        if not os.path.exists(os.path.join(dst_path, study_uid)):
            count += 1
            print
            count, src_path
            os.system("cp -rf {} {}".format(src_path, dst_path))