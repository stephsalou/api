
#-------- import ---------# 
import requests
import json

import functions

#-------code -----------#
url="https://jsonplaceholder.typicode.com/todos/1"
is_exist=functions.urlExist(url)
if is_exist['statut']:
    api_result=functions.getApi(url)
    print(api_result)
else:
    print(is_exist['message'])

print(is_exist)