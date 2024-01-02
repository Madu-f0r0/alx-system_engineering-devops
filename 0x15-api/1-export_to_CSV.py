#!/usr/bin/python3
"""This module fetches employer information from

`jsonplaceholder` API
"""

if __name__ == "__main__":
    import csv
    import json
    from sys import argv
    import urllib.request

    todos = "https://jsonplaceholder.typicode.com/todos"
    user = "https://jsonplaceholder.typicode.com/users"

    user_url = f"{user}/{argv[1]}"
    with urllib.request.urlopen(user_url) as response:
        user_details_json = response.read()
        user_details_python = json.loads(user_details_json)
        username = user_details_python.get("username")
        user_id = user_details_python.get("id")

    todos_url = f"{todos}?userId={argv[1]}"
    with urllib.request.urlopen(todos_url) as response:
        all_tasks_json = response.read()
        all_tasks = json.loads(all_tasks_json)

    with open("{}.csv".format(user_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, str(t.get("completed")), str(t.get("title"))]
            ) for t in all_tasks]
