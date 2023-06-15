#!/usr/bin/python3
""" script to export data in the JSON format. """
from requests import get
from json import dump


if __name__ == "__main__":
    ''' export data in the JSON format '''

    url = 'https://jsonplaceholder.typicode.com/users'
    users = get(url).json()
    u_all = {}
    for user in users:
        u_all[user.get("id")] = []
        url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
        url = url.format(user.get("id"))
        tasks = get(url).json()
        for task in tasks:
            u_all[user.get("id")].append({"task": task.get("title"),
                                          "completed": task.get("completed"),
                                          "username": user.get("username")})
    with open("todo_all_employees.json", "w") as f:
        dump(u_all, f)
