#!/usr/bin/python3
"""
0x15. API
Python
Scripting
Back-end
API
"""
import json
import requests
from sys import argv


def getData(id):
    """
    0. Gather data from an API
    using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_data = requests.get(f"{base_url}/users/{id if id else argv[1]}/todos")
    user_info = requests.get(f"{base_url}/users/{id if id else argv[1]}")
    if user_data.status_code == 200 and user_info.status_code == 200:
        data = user_data.json()
        info = user_info.json()
        return (data, info)
    return (None, None)


if __name__ == "__main__":
    """
     0. Gather data from an API
     using this REST API, for a given employee ID,
     export data in the JSON format.
     """

    data, info = getData(argv[1])
    if data and info:
        with open(f"{argv[1]}.json", 'w', newline='') as f:
            a = {
                    info.get("userId"): [{
                        "task": d.get("title"),
                        "completed": str(d.get("completed")),
                        "username": info.get("username")
                    } for d in data]
                    }
            print(a)
            json.dump(a, f)
