#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress """
from requests import get
from sys import argv


if __name__ == "__main__":
    ''' returns employee TODO list '''

    if len(argv) != 2:
        exit(1)

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    res = get(url).json()
    print("Employee {} is done with tasks".format(res.get("name")), end="")
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url = url.format(argv[1])
    tasks = get(url).json()
    complete = []
    for task in tasks:
        if task.get("completed"):
            complete.append(task)
    print("({}/{}):".format(len(complete), len(tasks)))
    for task in complete:
        print("\t {}".format(task.get("title")))
