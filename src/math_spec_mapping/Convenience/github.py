import os
import requests


def write_scaffold_to_github_issues(scaffolder_folder, repo_owner, repository_name):
    folders = [
        x
        for x in os.listdir(scaffolder_folder)
        if os.path.isdir(scaffolder_folder + "/" + x)
    ]
    for folder in folders:
        issue_name = "Write {} from MSML Scaffold".format(folder)
        checklist = [
            x[:-3]
            for x in os.listdir(scaffolder_folder + "/" + folder)
            if x.endswith(".md")
        ]
        checklist = ["- [ ] " + x for x in checklist]
        checklist = "\n".join(checklist)

        print(
            requests.post(
                "https://api.github.com/repos/{}/{}/issues".format(
                    repo_owner, repository_name
                ),
                data={"title": issue_name, "body": checklist},
            ).text
        )
