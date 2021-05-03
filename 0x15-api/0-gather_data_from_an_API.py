#!/usr/bin/python3
'''Given employee ID, returns information about his/her TODO list progress'''
from sys import argv
import json
import requests

url_users = "https://jsonplaceholder.typicode.com/users"
employee_id = argv[1]
employee = requests.get("{}/{}".format(url_users, employee_id))
employee_obj = json.loads(employee.text)
tasks = requests.get("https://jsonplaceholder.typicode.com/todos/")
tasks_obj = json.loads(tasks.text)
n_total = 0
n_done = 0
text = ""
for task in tasks_obj:
    if task['userId'] == int(employee_id):
        if task['completed'] is True:
            n_done += 1
            text += "\t {}\n".format(task['title'])
        n_total += 1
print("Employee {} is done with tasks({}/{}):".format(employee_obj['name'],
                                                      n_done, n_total))
print(text, end="")
