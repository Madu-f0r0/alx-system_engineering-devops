#!/usr/bin/python3
"""This module fetches employer information from

`jsonplaceholder` API
"""

if __name__ == "__main__":
    import json
    from sys import argv
    import urllib.request

    todos = "https://jsonplaceholder.typicode.com/todos"
    user = "https://jsonplaceholder.typicode.com/users"

    user_id = argv[1]
    user_url = f"{user}/{argv[1]}"
    with urllib.request.urlopen(user_url) as response:
        user_details_json = response.read()
        user_details_python = json.loads(user_details_json)
        username = user_details_python.get("username")

    todos_url = f"{todos}?userId={argv[1]}"
    with urllib.request.urlopen(todos_url) as response:
        all_tasks_json = response.read()
        all_tasks = json.loads(all_tasks_json)

        tasks_list = [{"task": t.get("title"),
                       "completed": t.get("completed"),
                       "username": username
                       }
                      for t in all_tasks
                      ]

        task_dict = {user_id: tasks_list}

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(task_dict, json_file)
