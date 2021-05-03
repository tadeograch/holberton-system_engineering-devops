#!/usr/bin/python3

import csv
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

    with open('{}.csv'.format(employee_id), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',',
                                     quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks_obj:
            if task['userId'] == int(employee_id):
                employee_writer.writerow([employee_id,
                                         employee_obj['username'],
                                         task['completed'],
                                         task['title']])
