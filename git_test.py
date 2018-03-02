'''
from github import Github

g = Github("andyppbb@gmail.com", "jack7820")
for repo in g.get_user().get_repos():
    print(repo.name)
'''
from datetime import datetime
from git import Repo
repo_dir = ''
repo = Repo(repo_dir)
repo.git.add(A=True)
repo.index.commit(str(datetime.now()))
origin = repo.remote('origin')
origin.push()
