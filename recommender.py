from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def recommend_task(df):

    if len(df) < 2:
        return None

    X = df[["Priority"]]
    y = df["Completed"]

    model = DecisionTreeClassifier()

    model.fit(X, y)

    pending_tasks = df[df["Completed"] == 0]

    if pending_tasks.empty:
        return None

    recommended = pending_tasks.sort_values(
        by="Priority",
        ascending=False
    )

    return recommended.iloc[0]["Task"]
