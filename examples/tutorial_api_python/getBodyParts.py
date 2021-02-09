#Archivo main
# import classifyParts from ./jsonToCsv.py
import jsonToCsv
import readJsons
import os, json, re
import pandas as pd

from collections import OrderedDict


body_parts = ["Nose.x", "Nose.y", "Nose.confidence","Neck.x","Neck.y","Neck.confidence","RShoulder.x","RShoulder.y","RShoulder.confidence","RElbow.x","RElbow.y","RElbow.confidence","RWrist.x","RWrist.y","RWrist.confidence",
            "LShoulder.x", "LShoulder.y", "LShoulder.confidence","LElbow.x","LElbow.y","LElbow.confidence","LWrist.x","LWrist.y","LWrist.confidence","MidHip.x","MidHip.y","MidHip.confidence","RHip.x","RHip.y","RHip.confidence",
    "RKnee.x","RKnee.y","RKnee.confidence","RAnkle.x","RAnkle.y","RAnkle.confidence","LHip.x","LHip.y","LHip.confidence","LKnee.x","LKnee.y","LKnee.confidence","LAnkle.x","LAnkle.y","LAnkle.confidence","REye.x","REye.y","REye.confidence",
    "LEye.x","LEye.y","LEye.confidence","REar.x","REar.y","REar.confidence","LEar.x","LEar.y","LEar.confidence","LBigToe.x","LBigToe.y","LBigToe.confidence","LSmallToe.x","LSmallToe.y","LSmallToe.confidence",
    "LHeel.x","LHeel.y","LHeel.confidence","RBigToe.x","RBigToe.y","RBigToe.confidence","RSmallToe.x","RSmallToe.y","RSmallToe.confidence","RHeel.x","RHeel.y", "RHeel.confidence"]

path = 'D:\mat\output_jsons'
d = {}

for x in readJsons.importJSONS(path):
    with open(path+'\\'+x+'_keypoints.json') as f:
        data = json.load(f)
        d[x] = jsonToCsv.classifyParts(data)
df1 = pd.DataFrame.from_dict(data=OrderedDict(d.items()),  orient='index',columns=body_parts)
df1.to_csv(path+"\\csvxx.csv")

#Link de acceso 
#'D:\mat\output_jsons'
#https://192.168.1.131:8888/







