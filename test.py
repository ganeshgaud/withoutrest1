from requests import *
import json
BASE_URL='http://127.0.0.1:8000/'
# ENDPOINT='api/'
# end=input("Enter Endpoint:")
# def get_resource(id):
#     ENDPOINT='api/'
#     resp=get(BASE_URL+ENDPOINT+str(id)+'/')
#     data=resp.json()
#     print(resp.status_code)
#     for i in data:
#         print("**********************************************")
#         for k,v in i.items():
#             print(k,"==",v)
#     # print(data)
#
# def get_resource_all():
#     ENDPOINT='api/'
#     resp=get(BASE_URL+ENDPOINT)
#     data=resp.json()
#     for i in data:
#         print("**********************************************")
#         for k,v in i.items():
#             print(k,"==",v)
#     # print(data)
#
# def create_resource():
#     ENDPOINT='api/'
#     new_std={
#     'Name':'Pradhyanesh',
#     'Father_Name':'Ganesh',
#     'Cell_no':7276153095,
#     'Address':'Mumbai',
#     }
#     resp=post(BASE_URL+ENDPOINT,data=json.dumps(new_std))
#     print(resp.status_code)
#     print(resp.json())
#
# def update_resource(id):
#     ENDPOINT='api/'
#     std={
#     'Cell_no':1234567891,
#     'Address':'Karimnagar'
#     }
#     resp=put(BASE_URL+ENDPOINT+str(id)+'/',data=json.dumps(std))
#     print(resp.status_code)
#     print(resp.json())
#
# def delete_resource(id):
#     ENDPOINT='api/'
#     resp=delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())

# Resource by one Url

def get_resource(id=None):
    ENDPOINT='allinone/'
    d={}
    if id is not None:
        d={
        'id':id,
        }
    resp=get(BASE_URL+ENDPOINT,data=json.dumps(d))
    print(resp.status_code)
    print(resp.json())

def create_resource(id):
    ENDPOINT='allinone/'
    new_std={
    'Name':'Sunny',
    'Father_Name':'Bunny',
    'Cell_no':7276153095,
    'Address':'Mumbai',
    }
    resp=post(BASE_URL+ENDPOINT,data=json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())

def update_resource(id):
    ENDPOINT='allinone/'
    std={
    'id':id,
    'Cell_no':1234567891,
    'Address':'Karimnagar',
    }
    resp=put(BASE_URL+ENDPOINT,data=json.dumps(std))
    print(resp.status_code)
    print(resp.json())

def create_resource():
    ENDPOINT='allinone/'
    new_std={
    'Name':'Micky',
    'Father_Name':'Ganesh',
    'Cell_no':9730797196,
    'Address':'Hyd',
    }
    resp=post(BASE_URL+ENDPOINT,data=json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())

def delete_resource(id):
    ENDPOINT='allinone/'
    new={
    'id':id,
    }
    resp=delete(BASE_URL+ENDPOINT,data=json.dumps(new))
    print(resp.status_code)
    print(resp.json())

delete_resource(23)
