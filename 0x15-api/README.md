# 0x15. API


## Background Context

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

## Resources
Read or watch:

* [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
* [What is an API](https://www.webopedia.com/definitions/api/)
* [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
* [What is a REST API](https://www.sitepoint.com/rest-api/)
* [What are microservices](https://smartbear.com/solutions/microservices/)
* [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://www.python.org/dev/peps/pep-0008/)

## Tasks

## [0. Gather data from an API](./0-gather_data_from_an_API.py)
Write a Python script that, using this [REST API](https://jsonplaceholder.typicode.com/), for a given employee ID, returns information about his/her TODO list progress.

Requirements:

* You must use urllib or requests module
* The script must accept an integer as a parameter, which is the employee ID
* The script must display on the standard output the employee TODO list progress in this exact format:
   + First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        EMPLOYEE_NAME: name of the employee
        NUMBER_OF_DONE_TASKS: number of completed tasks
        TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
   + Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

Example:
```
@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
@ubuntu$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
@ubuntu$
@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr " " "S" | tr "\t" "T" 
Employee Patricia Lebsack is done with tasks(6/20):
TSodit optio omnis qui sunt
TSdoloremque aut dolores quidem fuga qui nulla
TSsint amet quia totam corporis qui exercitationem commodi
TSsequi dolorem sed
TSeum ipsa maxime ut
TStempore molestias dolores rerum sequi voluptates ipsum consequatur
@ubuntu$
```

## [1. Export to CSV](./1-export_to_CSV.py)
Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

* Records all tasks that are owned by this employee
* Format must be: 
        "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
* File name must be: 
        USER_ID.csv

Example:

> python3 1-export_to_CSV.py 2

> cat 2.csv

## [2. Export to JSON](./2-export_to_JSON.py)
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

* Records all tasks that are owned by this employee
* Format must be:                        
        { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
* File name must be: 
        USER_ID.json
Example:

> python3 2-export_to_JSON.py 2

> cat 2.json

## [3. Dictionary of list of dictionaries](./3-dictionary_of_list_of_dictionaries.py)
Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

* Records all tasks from all employees
* Format must be: 
        { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
* File name must be: 
        todo_all_employees.json
Example:
> python3 3-dictionary_of_list_of_dictionaries.py

> cat todo_all_employees.json
