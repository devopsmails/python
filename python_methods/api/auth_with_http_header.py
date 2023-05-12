Authenticating API with HTTP Header:
  
  - Helps to hide the auth token from sniffing.
  
  ex:
    
import requests

pixel_endpoint = "https://pixe.la/v1/users"
TOKEN = "12345678a9"
USERNAME = "suresh1"
user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "notMinor": "yes",
    "agreeTermsOfService": "yes",

}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Cycling Habbit",
    "unit": 'Km',
    "type": "float",
    "color": "shibafu",
}

headers = {                                                 # <=================
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint,json=graph_config, headers=headers) <=================
print(response.text)

https://pixe.la/v1/users/suresh1/graphs/graph2.html
