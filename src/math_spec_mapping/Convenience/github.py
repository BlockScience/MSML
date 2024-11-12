import os


def write_scaffold_to_github_issues(scaffolder_folder):
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
        print(checklist)
