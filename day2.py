# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:37:36 2021

@author: 91798
"""


######## REST API in python ##############
'''
REST API --  Representational State Transfer Application Programming Interface

-used to retrieve data from remote websites. 
-To make a request to a remote web server and retrieve data, 
-we make use of the URL endpoint from where the API is being served. 
-Each URL is called a request and the data that is sent back is called a response.
- uses HTTP requests to GET, PUT, POST and DELETE data.
GET — Get a resource from a server.
POST — Create a new resource on the server.
PUT, PATCH — Update a request on the server.
DELETE — Delete a resource from the server.


Why use an API instead of a static dataset you can download?
-Data is constantly changing
-You want a small piece of a much larger pool of data


The ‘Request’---
Most commonly used request is the GET request which is used to retrieve data.

E.g.- https://www.google.com/maps.
/maps is the endpoint, https://www.google.com is the starting URL.


JSON Data
JSON is the primary format in which data is passed back and forth to APIs and most API servers will send their responses in JSON format — a single string containing a JSON object.
JSON is a way to encode data structures like lists and dictionaries to strings that ensure that they are easily readable by machines.
So, lists and dictionaries can be converted to JSON and strings can be converted to lists and dictionaries.
JSON looks much like a dictionary in Python, with key-value pairs stored.


Status code ------


200: Everything went okay, and the result has been returned (if any).
301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
404: The resource you tried to access wasn’t found on the server.
503: The server is not ready to handle the request.


json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.

'''

#end point = /movie/{movie_id}
api_key="JGJGHJGHJGJH87878989GHGYY"
movie_id=500
api_version=3
api_base_url= f"https://api.themoviedb.org/{api_version}"
endpoint_path= f"/movie/{movie_id}"
end_point= f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(end_point)


import json
import requests

def to_json(obj):
    data = json.dumps(obj, sort_keys=True,indent=4 )
    print(data)
    
#http://api.open-notify.org/astros.json   
response = requests.get("https://api.publicapis.org/entries")
print(response.status_code)
print(response.json())

#to_json(response.json())
to_json(response.json()['entries'])


########### Post request ###############
import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)
print(x)


import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 140, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(response.json())


import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()


import requests
import json
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 11, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.json()
#{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

print(response.status_code)



######### post
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()
#{'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}

todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
response.json()
#{'userId': 1, 'title': 'Wash car', 'completed': True, 'id': 10}

response.status_code