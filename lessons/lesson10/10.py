import requests

# URL для роботи з ресурсами
base_url = 'https://jsonplaceholder.typicode.com/posts'
resource_url = f"{base_url}/1"

# GET
print("GET----------------")
response_get = requests.get(url=resource_url)
print(f"Status: {response_get.status_code}")
print(response_get.text)

# POST
print("POST----------------")
body = {
    "userId": 12,
    "title": "test",
    "body": "test"
}
response_post = requests.post(url=base_url, json=body)
print(f"Status: {response_post.status_code}")
print(response_post.text)

# PUT
print("PUT----------------")
data_put = {
    "id": 1,
    "userId": 1,
    "title": "test_put",
    "body": "updated content"
}
response_put = requests.put(url=resource_url, json=data_put)
print(f"Status: {response_put.status_code}")
print(response_put.text)

# PATCH
print("PATCH----------------")
data_patch = {
    "title": "patched title"
}
response_patch = requests.patch(url=resource_url, json=data_patch)
print(f"Status: {response_patch.status_code}")
print(response_patch.text)

# DELETE
print("DELETE----------------")
response_delete = requests.delete(url=resource_url)
print(f"Status: {response_delete.status_code}")
print(response_delete.text)
