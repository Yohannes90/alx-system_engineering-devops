#!/usr/bin/python3
""" Using the task #0, extend to export data in the JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = user.get("username")

    with open("{}.json".format(sys.argv[1]), "w", newline="") as jsonfile:
        json.dump({sys.argv[1]: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in todos]}, jsonfile)
