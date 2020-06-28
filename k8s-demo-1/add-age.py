from pymongo import MongoClient
import pymongo
from pymongo.bulk import ObjectId
import csv
from datetime import date
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from glob import glob
import os


client = MongoClient('192.168.1.230', 27017)
db = client.diagnosis
patient_study = db.patient_study

if __name__ == '__main__':
    df = pd.read_csv("./MNreport198118-0705-0708_predict_new+.csv")
    patient_uids = df.values[:,1]

    # patient_studys = list(patient_study.find({'patient_id': {'$in': list(patient_uids)}}))

    patient_result = []
    for patient_uid in patient_uids:
        patient_studys = patient_study.find({'patient_id':patient_uid}).sort('create_time', pymongo.ASCENDING)
        # for patient_study in list(patient_studys):
                # if patient_study['patient_id'] == patient_uid:
        patient_result.append(patient_studys[0]['age'])
        print(patient_uid, patient_studys[0]['age'])
        df.to_csv('./MNreport198118-0705-0708_predict_new+age.csv', index=False, sep=',')