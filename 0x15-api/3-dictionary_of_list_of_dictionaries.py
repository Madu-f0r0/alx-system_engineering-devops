#!/usr/bin/python3
"""This module fetches employer information from

`jsonplaceholder` API
"""

if __name__ == "__main__":
    import json
    import urllib.request

    todos = "https://jsonplaceholder.typicode.com/todos"
    user_url = "https://jsonplaceholder.typicode.com/users"

    # user_url = f"{user}/{argv[1]}"
    with urllib.request.urlopen(user_url) as response:
        user_details_json = response.read()
        user_details_python = json.loads(user_details_json)
        user_id_name = [(str(user.get("id")), user.get("username"))
                        for user in user_details_python
                        ]

    task_dict = {}
    for user in user_id_name:
        todos_url = f"{todos}?userId={user[0]}"
        with urllib.request.urlopen(todos_url) as response:
            all_tasks_json = response.read()
            all_tasks = json.loads(all_tasks_json)

            tasks_list = [{"username": user[1],
                           "task": t.get("title"),
                           "completed": t.get("completed"),
                           }
                          for t in all_tasks
                          ]

            task_dict.update({user[0]: tasks_list})

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(task_dict, json_file)
