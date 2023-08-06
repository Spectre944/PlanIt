# This Python file uses the following encoding: utf-8
import json

key_task        = 'task'
key_subtusk     = 'subtusk'
key_isCompleted = 'completed'
key_startDate   = 'startDate'
key_endDate     = 'endDate'
key_desription  = 'desription'



class SceJsonWork:
    def __init__(self):
        pass

    def loadJson(self, path):
        with open(path) as file:
            document = json.load(file)
            print(document)


    def getByKey(self, key):
        return key_task
