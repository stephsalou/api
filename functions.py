#-------- import ---------# 
import requests
import json

#-------code -----------#
def getApi(url):
    is_sucess=False
    result={}
    data={}
    try:
        req=requests.get(url)
        print(req.status_code)  
        if req.status_code==200:
            data=req.text
            is_sucess=True
            result['message']="données récupérer avec succes"
        else:
            is_sucess=False
            result['message']="impossible de recupéré les données"
    except:
        is_sucess=False
        result['message']="l'url entrée n'existe pas"
    result['succes']=is_sucess
    result['data']=data
    return result


def urlExist(url):
    result={}
    exist=False
    try:
        requests.get(url)
        exist=True
        result['message']="l'url demandé est disponible"
    except :
        exist=False
        result['message']="l'url n'existe pas"
    result['statut']=exist
    return result