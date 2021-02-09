import json
import pandas as pd
import csv

def classifyParts(data):

    people = data["people"]
    result = people[0]['pose_keypoints_2d']
    return result 


# en otro .py bucle que recorra todos los json de outputs, guarde en diccionario nombre del json, dict de puntos, y calificacion de bien o mal
# creo que tendiamos que tener el arbol d outputs como 
# outputs/bien/json...
# outputs/mal/json...