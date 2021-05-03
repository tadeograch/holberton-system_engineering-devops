#!/usr/bin/python3
'''Export data in the JSON format'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users"
    employee_id = argv[1]
    employee = requests.get("{}/{}".format(url_users, employee_id))
    employee_obj = json.loads(employee.text)
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/")
    tasks_obj = json.loads(tasks.text)
    data = {}
    data[employee_id] = []

    for task in tasks_obj:
        if task['userId'] == int(employee_id):
            data[employee_id].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_obj['username'],
            })

    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(data, file)
