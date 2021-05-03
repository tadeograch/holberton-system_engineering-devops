#!/usr/bin/python3
'''Export data in the JSON format'''
import json
import requests

if __name__ == "__main__":
    url_users = "https://jsonplaceholder.typicode.com/users"
    employees = requests.get(url_users)
    employee_obj = json.loads(employees.text)
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/")
    tasks_obj = json.loads(tasks.text)
    data = {}

    for employee in employee_obj:
        employee_id = str(employee['id'])
        data[employee_id] = []
        for task in tasks_obj:
            if task['userId'] == int(employee_id):
                data[employee_id].append({
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": employee['username'],
                })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
