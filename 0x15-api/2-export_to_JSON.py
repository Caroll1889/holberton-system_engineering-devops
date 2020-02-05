#!/usr/bin/python3
# Python script that returns information about his/her TODO list progress

import requests
import sys
import json


if __name__ == "__main__":

    employ_Id = sys.argv[1]

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(employ_Id)).json()

    task = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(employ_Id)).json()

    data = {}
    new_list = []
    username = req.get('username')

    with open("{}.json".format(employ_Id), "w") as file:

        for i in task:
            new_dict = {}

            new_dict['username'] = username
            new_dict['task'] = i.get('title')
            new_dict['completed'] = i.get('completed')

            new_list.append(new_dict)

        data[employ_Id] = new_list
        json.dump(data, file)
