import pandas as pd
import os

FILE_NAME = "tasks.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Task", "Priority", "Completed"])
        df.to_csv(FILE_NAME, index=False)

def add_task(task, priority):
    df = pd.read_csv(FILE_NAME)

    new_task = {
        "Task": task,
        "Priority": priority,
        "Completed": 0
    }

    df.loc[len(df)] = new_task
    df.to_csv(FILE_NAME, index=False)

def remove_task(task_name):
    df = pd.read_csv(FILE_NAME)

    df = df[df["Task"] != task_name]

    df.to_csv(FILE_NAME, index=False)

def list_tasks():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\nNo Tasks Available.\n")
        return

    print("\nCurrent Tasks:\n")
    print(df)

def get_tasks():
    return pd.read_csv(FILE_NAME)
