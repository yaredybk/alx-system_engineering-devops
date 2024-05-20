#!/usr/bin/python3
"""
 0. Gather data from an API
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
 """
import requests
from sys import argv


base_url = "https://jsonplaceholder.typicode.com"
user_data = requests.get(f"{base_url}/users/{argv[1]}/todos")
user_info = requests.get(f"{base_url}/users/{argv[1]}")

if user_data.status_code == 200 and user_info.status_code == 200:
    data = user_data.json()
    info = user_info.json()
    completed_tasks = 0
    total_tasks = 0
    for task in data:
        total_tasks += 1
        completed_tasks += 1 if (task["completed"]) else 0
    print(f"Employee {info['name']}  is done with tasks\
            ({completed_tasks}/{total_tasks}):")
    [print(f"\t {t['title']}") for t in data if t["completed"]]
