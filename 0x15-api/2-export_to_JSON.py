#!/usr/bin/python3
""" script to export data in the JSON format. """
from sys import argv
from requests import get
from json import dump


if __name__ == "__main__":
    ''' export data in the JSON format '''

    if len(argv) != 2:
        exit(1)

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    res = get(url).json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url = url.format(argv[1])
    tasks = get(url).json()
    user_info = {argv[1]: []}
    for task in tasks:
        user_info[argv[1]].append({"username": res.get("username"),
                                   "completed": task.get("completed"),
                                   "task": task.get("title")})
    with open("{}.json".format(argv[1]), "w") as f:
        dump(user_info, f)
