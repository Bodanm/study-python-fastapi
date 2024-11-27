import requests

base_url = 'https://jsonplaceholder.typicode.com/comments'

url_param_1 = "https://jsonplaceholder.typicode.com/comments?postId=2"

params_url = ["?id=1"]


def save_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# resource_get = f"{base_url}/comments/3"
# try:
#     # GET WITH PARAMS URL
#     response_get = requests.get(url=base_url + params_url[0])
#
#     if response_get.status_code == 200:
#         print("GET WITH PARAMS URL ---------------- sucsesfully completed:")
#         print(response_get.headers)
#         print(response_get.text)
#         save_to_file("response_get_url.txt", response_get.text)
#     else:
#         print(f"its Error, error kod is: {response_get.status_code}")
# except  requests.exceptions.RequestException as e:
#     print(f"There is a error when request was send: {e}")


params = {
    "id": 15
}

# GET WITH PARAMS
try:
    # GET WITH PARAMS URL
    response_get = requests.get(url=base_url, params=params)

    if response_get.status_code == 200:
        print("GET WITH PARAMS ---------------- sucsesfully completed:")
        print(response_get.headers)
        print(response_get.text)
        save_to_file("response_get.txt", response_get.text)
    else:
        print(f"its Error, error kod is: {response_get.status_code}")
except  requests.exceptions.RequestException as e:
    print(f"There is a error when request get was send: {e}")

# POST
try:

    body = {
        "name": "Tom",
        "password": "Tom123"

    }
    response_post = requests.post(url=base_url, json=body)
    if response_post.status_code == 201:
        print("POST ADD NAME AND PASSWORD---------------- sucsesfully completed:")
        print(response_post.headers)
        print(response_post.text)
        save_to_file("response_post.txt", response_post.text)
    else:
        print(f"its Error, error kod is: {response_post.status_code}")
except requests.exceptions.RequestException as e:
    print(f"There is a error when request post was send: {e}")
