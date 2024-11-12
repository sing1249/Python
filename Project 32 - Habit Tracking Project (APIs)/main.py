import requests
from datetime import datetime

USERNAME = "talwinder"
TOKEN = "dfjbdskffbzbjv"
GRAPH_ID = "graph1"
#Creating a user at pixela using POST request.
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_parameters) #To complete the post request.
print(response.text)

#Creating a graph

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Meditation Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

#Posting a pixel to the graph

today = datetime(year=2024, month=11, day=11)
#print(today.strftime("%Y%m%d"))
addition_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
additon_params = {
    "date": today.strftime("%Y%m%d"), #Using strftime method, making the date in required format as per API doc.
    "quantity": "15",
}

response = requests.post(url=addition_endpoint, json=additon_params, headers=headers)
print(response.text)


#Updating the data that is already posted using put requests.
update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
update_params = {
    "quantity": "11",
}

response = requests.put(url=update_endpoint, json=update_params, headers=headers)
print(response.text)


#Deleting the data - Will delete data for yesterday as today is getting the date of yesterday.
delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
