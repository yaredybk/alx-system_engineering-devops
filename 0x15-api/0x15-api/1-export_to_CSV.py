#!/usr/bin/python3
"""
0x15. API
Python
Scripting
Back-end
API
"""
import requests
from sys import argv
from 0-gather_data_from_an_API import getData


if __name__ == "__main__":
    """
     0. Gather data from an API
     using this REST API, for a given employee ID,
     export data in the CSV format.
     """
     with open(f"{argv[1]}.csv", 'w', newline='') f:
         writter = csv.writer(f)
         writter.writerows([
    data ,info = getData(argv[1])
    if data and info:
        completed_tasks = 0
        total_tasks = 0
        for task in data:
            total_tasks += 1
            completed_tasks += 1 if (task["completed"]) else 0
        print(f"Employee {info['name']}  is done with tasks\
                ({completed_tasks}/{total_tasks}):")
        [print(f"\t {t['title']}") for t in data if t["completed"]]
