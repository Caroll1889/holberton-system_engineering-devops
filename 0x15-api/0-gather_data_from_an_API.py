#!/usr/bin/python3
# Python script that returns information about his/her TODO list progress

import requests
import sys

if __name__ == "__main__":

    employ_Id = sys.argv[1]

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(employ_Id)).json()

    task = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(employ_Id)).json()

    task_list = []

    for tasks in task:
        if tasks.get('completed') is True:
            task_list.append(tasks.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(req.get('name'),
          len(task_list), len(task)))
    for tasks in task_list:
        print("\t {}".format(tasks))
