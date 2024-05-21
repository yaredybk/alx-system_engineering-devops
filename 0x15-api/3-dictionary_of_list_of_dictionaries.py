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


def getData():
    """
    0. Gather data from an API
    using this REST API, for all employees,
    returns information about all TODO list progress.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    all_data = requests.get(f"{base_url}/todos")
    all_info = requests.get(f"{base_url}/users")
    if all_data.status_code == 200 and all_info.status_code == 200:
        data = all_data.json()
        info = all_info.json()
        return (data, info)
    return (None, None)


if __name__ == "__main__":
    """
     0. Gather data from an API
     using this REST API, for all employees,
     export data in the JSON format.
     """

    data, info = getData()
    if data and info:
        with open(f"todo_all_employees.json", 'w', newline='') as f:
            u = {
                    d.get("id"): {
                        "username": d.get("name")
                        }
                    for d in info
                    }
            a = {}

            for d in data:
                id = d.get("userId")
                if a.get(id):
                    a[id].append({
                        "username": u.get(id, {}).get("username"),
                        "task": d.get("title"),
                        "completed": d.get("completed")
                        })
                else:
                    a[id] = [{
                        "username": u.get(id, {}).get("username"),
                        "task": d.get("title"),
                        "completed": d.get("completed")
                    }]
            json.dump(a, f)
