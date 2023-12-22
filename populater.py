import os
import requests
from dotenv import load_dotenv

from task_list import tasks


load_dotenv(override=True)

BASE_URL = "http://127.0.0.1:8000/api"


def auth():
    user_details = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("USER_PWD"),
    }
    r = requests.post(BASE_URL + "/auth/login", user_details)
    if r.status_code == 200:
        access_token = r.json()["access"]
        return access_token
    return None


token = auth()
if token:
    for count, task in enumerate(tasks):
        r = requests.post(
            url=BASE_URL + "/tasks",
            data=task,
            headers={"Authorization": f"Bearer {token}"},
        )
        if r.status_code == 201:
            print(f"Added {count+1} task(s) of {len(tasks)}...")
        elif r.status_code == 401:
            token = auth()
        else:
            print(r.json())

else:
    print("Authentication failed!\n")
