import os
import requests
from github import Github, Auth
import pandas as pd
from dotenv import load_dotenv


def write_scaffold_to_github_issues(
    scaffolder_folder, repo_owner, repository_name, access_token
):
    folders = [
        x
        for x in os.listdir(scaffolder_folder)
        if os.path.isdir(scaffolder_folder + "/" + x)
    ]
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": "Bearer {}".format(access_token),
    }
    for folder in folders:
        issue_name = "Write {} from MSML Scaffold".format(folder)
        checklist = [
            x[:-3]
            for x in os.listdir(scaffolder_folder + "/" + folder)
            if x.endswith(".md")
        ]
        checklist = ["- [ ] " + x for x in checklist]
        checklist = "\n".join(checklist)

        requests.post(
            "https://api.github.com/repos/{}/{}/issues".format(
                repo_owner, repository_name
            ),
            headers=headers,
            json={"title": issue_name, "body": checklist},
        )


def find_open_issues():
    load_dotenv()
    g = Github(auth=Auth.Token(os.getenv("GITHUB_TOKEN")))
    repo = g.get_repo("BlockScience/MSML")
    open_issues = repo.get_issues(state="open")
    open_issues = list(open_issues)

    df = pd.DataFrame(
        [[x.title, x.labels, x.html_url, x.milestone] for x in open_issues],
        columns=["Name", "Labels", "URL", "Milestone"],
    )
    df["Milestone"] = df["Milestone"].apply(lambda x: x.title if x else None)
    df = df.join(
        df["Labels"]
        .apply(lambda x: {y.name: True for y in x})
        .apply(pd.Series)
        .fillna(False)
    )

    empty = df[df["Labels"].apply(lambda x: len(x)) == 0]
    empty = empty[~empty["URL"].str.contains("MSML/pull")]
    assert len(empty) == 0, "Some issues do not have labels"

    return df, open_issues


def create_priority_label_matrix(df, exclude_milestones=None):
    if exclude_milestones:
        df = df[~df["Milestone"].isin(exclude_milestones)]
    priority_labels = ["High Priority", "Medium Priority", "Low Priority"]
    labels = list(df.columns[4:])
    labels = sorted([x for x in labels if x not in priority_labels])

    table = []
    for label in labels:
        row = []
        for priority in priority_labels:
            row.append(df[(df[priority]) & (df[label])])
        table.append(row)
    table = pd.DataFrame(table, index=labels, columns=priority_labels)
    table = table.applymap(
        lambda y: "\n".join(
            y.apply(lambda x: "[{}]({})".format(x["Name"], x["URL"]), axis=1).values
        )
    )
    return table


def create_milestone_label_matrix(df, exclude_milestones=None):
    if exclude_milestones:
        df = df[~df["Milestone"].isin(exclude_milestones)]
    priority_labels = ["High Priority", "Medium Priority", "Low Priority"]
    labels = list(df.columns[4:])
    labels = sorted([x for x in labels if x not in priority_labels])
    milestones = sorted(list(df[~pd.isnull(df["Milestone"])]["Milestone"].unique()))
    try:
        milestones = sorted(
            milestones,
            key=lambda x: int(x.split(".")[0][1:]) * 10000
            + int(x.split(".")[1]) * 100
            + int(x.split(".")[2]),
        )
    except:
        pass

    table = []
    for label in labels:
        row = []
        for milestone in milestones:
            row.append(df[(df["Milestone"] == milestone) & (df[label])])
        table.append(row)
    table = pd.DataFrame(table, index=labels, columns=milestones)
    table = table.applymap(
        lambda y: "\n".join(
            y.apply(lambda x: "[{}]({})".format(x["Name"], x["URL"]), axis=1).values
        )
    )
    return table
