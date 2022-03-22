import git
from os import path
import shutil


#TODO make it an args
WORKSPACE_PATH="git_test"

#clone repo
if path.exists(WORKSPACE_PATH) == True:
    shutil.rmtree(WORKSPACE_PATH)

git.Repo.clone_from("https://github.com/haithembentanfous/generate_html_from_json.git",WORKSPACE_PATH)


g = git.Git("/media/haithem/DATA/Haithem/works/test")
loginfo = g.log('--format=LOGS|%an-%ad-%s','--name-only')

print(loginfo)


#cleanup
if path.exists(WORKSPACE_PATH) == True:
    shutil.rmtree(WORKSPACE_PATH)