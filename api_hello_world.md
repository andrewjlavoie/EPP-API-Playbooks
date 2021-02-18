# API Hello World
Table of Contents
- Purpose
- Requirements
- Authorization
- Summary

## Purpose
The purpose of this page is to walk a user through the initial authorization to the Management Console API.

## Requirements
This guide is using Python 3.8 with the requests library.

## Authorization
To get started with the Management Console API the first thing we need to do is authenicate to the server. The MC APi is using Java Web Tokens for authoriation. These are session based authorizations, and a new token will need to be requested upon expiration.

### Get Token
To get our JWT we need to make a POST request with our username and password to the '/api/login'

With Python, we will need to first import the `requests` library.


`import requests`

Next we will need to create some variables with our information required for authorization.


`url = 'https://mc.hosted.endpointprotector.com/api/login'`
`headers = {'Content-Type': 'application/json'}`
`auth = {'username': 'root', 'password': 'rootpass')`

Now that we have defined our request headers and the authorization parameters, we will load them into a request. We want to store this request into a variable so we can export the token from the JSON returned.

`my_jwt = requests.post(url, headers=headers, json=auth)`

> If we `print` the above `my_jwt` variable we will see the HTTP response code:
> `<Response [200]>`
{.is-info}

To transfor our response into usable data, we wil apply the `json()` method.

`my_jwt = my_jwt.json()`

This will return `my_jwt` as a dictionary containing 1 key-value pair.:

`{'token': 'very long token'}`

### Using our Token in a GET call

For our example we will be requesting the list of connected EPP Servers. We will store our call into a variable and transform the data in one step.

`connected_servers = requests.get(
    'https://mc.hosted.endpointprotector.com/api/server',
    headers={'Authorization': jwt}
    ).json()`

This variable now contains a dictionary that contains all connected EPP core servers in the cluster. The output should be similar to:

`{'current_page': 1, 'items': [{'id': 1, 'name': 'EPP Hosted 1', 'description': 'Endpoint Protector - hosted environment', 'server_location': 'https://15.223.123.80:44333', 'client_id': 'client_id_epp_1', 'ip': '15.223.123.80', 'port': '443', 'created_at': None, 'updated_at': '2020-12-14 14:50:24', 'created_by': None, 'updated_by': None}, {'id': 2, 'name': 'EPP Hosted 2', 'description': 'Endpoint Protector - hosted environment', 'server_location': 'https://3.96.69.235:44333', 'client_id': 'client_id_epp_2', 'ip': '3.96.69.235', 'port': '443', 'created_at': None, 'updated_at': '2020-12-14 14:50:24', 'created_by': None, 'updated_by': None}], 'page_count': 1, 'items_per_page': 10, 'total_item_count': 2}`

### Summary

In this quick 'Hello World' example we walked through getting your Java Web Token and utilizing that toke in a GET API call.
Thank you!