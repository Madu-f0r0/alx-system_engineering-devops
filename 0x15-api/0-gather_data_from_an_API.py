#!/usr/bin/python3
"""This module fetches employer information from

`jsonplaceholder` API
"""

if __name__ == "__main__":
    import json
    import urllib.request
    from sys import argv

    todos = "https://jsonplaceholder.typicode.com/todos"
    user = "https://jsonplaceholder.typicode.com/users"

    user_url = f"{user}/{argv[1]}"
    with urllib.request.urlopen(user_url) as response:
        user_details_json = response.read()
        user_details_python = json.loads(user_details_json)
        employee_name = user_details_python.get("name")

    todos_url = f"{todos}?userId={argv[1]}"
    with urllib.request.urlopen(todos_url) as response:
        all_tasks_json = response.read()
        all_tasks = json.loads(all_tasks_json)

        tasks_done = [task for task in all_tasks if task.get("completed")]

        print("Employee {} is done with tasks({}/{}):".format(
              employee_name, len(tasks_done), len(all_tasks)))

        for task in tasks_done:
            print("\t {}".format(task.get("title")))
