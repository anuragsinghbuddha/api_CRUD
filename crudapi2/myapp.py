import requests
import json

URL="http://127.0.0.1:8000/studentapi/"
 
#read data
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id} 
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL ,headers=headers,data=json_data)
    data=r.json()
    print(data) 

#get_data()

#post/create data
def post_data():
    data={
        'name':'bala',
        'roll':2,
        'city':'purnia',
        
    }
    #above data is in python object hence convert in json and hit to url
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL ,headers=headers,data=json_data)
    data=r.json()
    print(data)

#post_data()

#put/update data
def update_data():
    data={
        'id':3,
        'roll':3,
        'name':'lalit',
        'city':'jaipur'
        
    }
    #above data is in python object hence convert in json and hit to url
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.put(url=URL ,headers=headers,data=json_data)
    data=r.json()
    print(data)

#update_data()

#delete/delete data 

def delete_data():
    data={
        'id':3, #only need to id ,which we wants to delete  
    }
    #above data is in python object hence convert in json and hit to url
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}

    r=requests.delete(url=URL ,headers=headers,data=json_data)
    data=r.json()
    print(data)

delete_data()



