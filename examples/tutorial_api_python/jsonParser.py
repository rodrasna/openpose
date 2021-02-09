import json
import pandas as pd
import csv

data = {
    "version":1.3,
    "people":[{
            "person_id":[-1],
            "pose_keypoints_2d":[
                740.208,323.205,0.843024,
                724.976,535.973,0.925195,
                567.027,551.315,0.801742,
                488.563,787.462,0.861453,
                417.763,1023.41,0.892556,
                905.738,535.333,0.905246,
                1015.61,771.538,0.859456,
                1094.12,968.706,0.930378,
                740.426,1039.57,0.745578,
                645.836,1047.11,0.758941,
                606.762,1448.64,0.800005,
                614.318,1786.71,0.845084,
                850.84,1039.34,0.768068,
                952.587,1409.5,0.833647,
                1023.63,1794.6,0.85775,
                716.612,283.683,0.957002,
                779.683,284.029,0.949846,
                653.935,315.157,0.892607,
                826.864,338.428,0.868423,
                1039.75,1889.25,0.764246,
                1102.12,1858.06,0.850881,
                984.358,1841.99,0.758332,
                527.564,1857.64,0.831243,
                504.308,1841.88,0.770281,
                654,1810.74,0.884812],
            "face_keypoints_2d":[],
            "hand_left_keypoints_2d":[],
            "hand_right_keypoints_2d":[],
            "pose_keypoints_3d":[],
            "face_keypoints_3d":[],
            "hand_left_keypoints_3d":[],
            "hand_right_keypoints_3d":[]
    }]
}
people = data["people"]
das = people[0]
# print(json.dumps(das["pose_keypoints_2d"]))

#divide each threesome and identify body parts

# csv:
# name, manox, manoy, muñecax, muñecay,...., calification

body_parts = ["Nose","Neck","RShoulder","RElbow","RWrist","LShoulder","LElbow","LWrist","MidHip","RHip",
"RKnee","RAnkle","LHip","LKnee","LAnkle","REye","LEye","REar","LEar","LBigToe","LSmallToe",
"LHeel","RBigToe","RSmallToe","RHeel","Background"]

result = {}

for i in range(0, 25):
    result[body_parts[i]+".x"] = das['pose_keypoints_2d'][i*3]
    result[body_parts[i]+".y"] = das['pose_keypoints_2d'][i*3+1]
    result[body_parts[i]+".prob"] = das['pose_keypoints_2d'][i*3+2] 
    
print(result.ndim)
df1 = pd.DataFrame(data=result, columns=body_parts)
df1.info()


# en otro .py bucle que recorra todos los json de outputs, guarde en diccionario nombre del json, dict de puntos, y calificacion de bien o mal
# creo que tendiamos que tener el arbol d outputs como 
# outputs/bien/json...
# outputs/mal/json...