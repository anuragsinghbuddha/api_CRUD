import requests
import json

URL="http://127.0.0.1:8000/studentapi/"
 
#read data
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id} 
    json_data=json.dumps(data)
    r=requests.get(url=URL ,data=json_data)
    data=r.json()
    print(data) 

#get_data()

#post/create data
def post_data():
    data={
        'name':'krishna',
        'roll':10,
        'city':'Mathura',
        
    }
    #above data is in python object hence convert in json and hit to url
    json_data=json.dumps(data)
    r=requests.post(url=URL ,data=json_data)
    data=r.json()
    print(data)

#post_data()

#put/update data
def update_data():
    data={
        'id':5,
        'name':'om',
        'city':'varansi'
        
    }
    #above data is in python object hence convert in json and hit to url
    json_data=json.dumps(data)
    r=requests.put(url=URL ,data=json_data)
    data=r.json()
    print(data)

update_data()

#delete/delete data 

def delete_data():
    data={
        'id':4, #only need to id ,which we wants to delete  
    }
    #above data is in python object hence convert in json and hit to url
    json_data=json.dumps(data)
    r=requests.delete(url=URL ,data=json_data)
    data=r.json()
    print(data)

#delete_data()



