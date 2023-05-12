#https://pixe.la/#
import requests
from datetime import datetime

pixel_endpoint = "https://pixe.la/v1/users"
TOKEN = "12345678a9"
USERNAME = "suresh1"
GRAPH = "graph2"
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
    "id": GRAPH,
    "name": "Cycling Habbit",
    "unit": 'Km',
    "type": "float",
    "color": "shibafu",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
print(response.text)

#The below are other api code requests we can use them by uncommenting them. 
request.post()
request.put()
request.delete()

# #https://pixe.la/v1/users/suresh1/graphs/graph2.html
# #adding a value to the pixel #https://docs.pixe.la/entry/post-pixel
# 
# today = datetime.now()
# formatted_date = today.strftime("%Y%m%d")
# 
# pixel_creating_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH}"
# pixel_config = {
#     "date": formatted_date,
#     "quantity": "9.7"
# }
# # response = requests.post(url=pixel_creating_endpoint, json= pixel_config, headers=headers)
# # print(response.text)
# 
# #Results: https://pixe.la/v1/users/suresh1/graphs/graph2.html

# updating_pixela_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH}/{formatted_date}"
# requsts_data = {
#     "quantity": "50.1"
# }
# # response = requests.put(url=updating_pixela_endpoint, json= requsts_data, headers=headers )
# #
# # print(response.text)
# 
# deleting_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
# #
# response = requests.delete(url=deleting_endpoint, headers=headers)
# print(response.text)
