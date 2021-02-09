from os import walk


import os, json
import pandas as pd



fileList = []
def importJSONS(path):
    json_files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
    for name in json_files:
        lista = [int(i) for i in name if i.isdigit()]
        result = ''.join(str(y) for y in lista)
        fileList.append(int(result))

    fileList.sort()
    return [str(i) for i in fileList]

