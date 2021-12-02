import json 
import pprint
import base64
import requests
import datetime
import traceback
from pprint import pprint
from scalpl import Cut

def loadfromJson(fileName):
    with open(fileName) as f:
        data = json.load(f)
    return data

def listDiff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))