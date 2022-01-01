import git
from os import path
import shutil


#clone repo

if path.exists("/media/haithem/DATA/Haithem/works/test") == True:
    shutil.rmtree("/media/haithem/DATA/Haithem/works/test")

git.Repo.clone_from("https://github.com/haithembentanfous/generate_html_from_json.git","/media/haithem/DATA/Haithem/works/test")


g = git.Git("/media/haithem/DATA/Haithem/works/test")
loginfo = g.log('--format=%an-%ad-%s')

print(loginfo)
