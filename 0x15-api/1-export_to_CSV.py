#!/usr/bin/python3
""" script to export data in the CSV format. """
from sys import argv
from requests import get
from csv import writer, QUOTE_ALL


if __name__ == "__main__":
    ''' export data in the CSV format '''

    if len(argv) != 2:
        exit(1)

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    res = get(url).json()
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url = url.format(argv[1])
    tasks = get(url).json()
    user_info = []
    for task in tasks:
        user_info.append([argv[1],
                          res.get("username"),
                          task.get("completed"),
                          task.get("title")])
    with open("{}.csv".format(argv[1]), "w") as f:
        writer = writer(f, quoting=QUOTE_ALL)
        writer.writerows(user_info)
