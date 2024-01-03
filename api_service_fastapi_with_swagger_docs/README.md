![Star Badge](https://img.shields.io/static/v1?style=flat&color=green&logo=python&label=MiniPy&message=%F0%9F%8C%9F%20If%20you%20found%20it%20useful) <a href="https://github.com/VinayakHegde">![Star Author](https://img.shields.io/static/v1?&style=flat&color=green&logo=github&label=Author&message=Vinayak%20Hegde)</a>

#  API Service using FastApi with Swagger Documentation

## 🛠️ Description
Api Service is a simple api service that exposes endpoints.

`GET: /api/v1/users` - returns a json with the list of users.
`POST: /api/v1/users` - creates a new user and returns a json with the user details.
`GET: /api/v1/users/<id>` - returns a json with the user details.
`PUT: /api/v1/users/<id>` - updates the user and returns a json with the user details.
`DELETE: /api/v1/users/<id>` - deletes the user and returns a json with the user details.

The Swagger documentation includes details for each endpoint, specifying parameters, request bodies, and expected responses. You can access the Swagger UI at `http://localhost:5000/api/v1` after running the Flask application.

## ⚙️ Modules Used

The program was created with `python3`, `flask`, `flask_restful` and `flasgger`.

use this for install pytube
`pip3 install -r requirements.txt`

## 🤖 How to run
`python3 main.py`
