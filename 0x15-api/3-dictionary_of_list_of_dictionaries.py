#!/usr/bin/python3
""" Using the task #0, extend to export data in the JSON format
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        json.dump({
            user.get("id"): [{
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            } for task in requests.get(url + "todos", params={"userId": user.get("id")}).json()]
        for user in users}, jsonfile)
