import requests
import os
from datetime import datetime

TOKEN = os.environ.get('PIXELA_TOKEN')
USERNAME = os.environ.get('PIXELA_USERNAME')
GRAPH_ID = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    'id': 'graph2',
    'name': 'Gym visit Graph',
    'unit': 'Days',
    'type': 'int',
    'color': 'kuro'
}
headers = {
    'X-USER-TOKEN': TOKEN
}

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

now = datetime.now()
today = now.strftime("%Y%m%d")
print(today)

# Post Data
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_config = {
    'date': today,
    'quantity': '7',

}
response = requests.post(url=post_endpoint, json=post_config, headers=headers)

# Update Data from grid
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_config = {

    'quantity': '9',
}
response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

# Delete Data from grid
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# response = requests.put(url=delete_endpoint, headers=headers)
# print(response.text)