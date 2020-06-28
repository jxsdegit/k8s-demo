import pandas as pd
import os
import numpy as np

series_uids = pd.read_csv("F:\\results(1).csv")['series_uid']
study_uids = pd.read_csv("F:\\results(1).csv")['study_uid']

ll = []

for i in series_uids:
    ll.append(i)
print(ll)
