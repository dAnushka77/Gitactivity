# Gitactivity

1) To initialize git -
   git init
   
2) To connect local code to the pre-existing repo -
   git remote add origin https://github.com/dAnushka77/Gitactivity.git
   
3) To check if repo has been added successfully -
   git remote -v
It should give output as below -
   origin  https://github.com/dAnushka77/Gitactivity.git (fetch)
   origin  https://github.com/dAnushka77/Gitactivity.git (push)
   
4) Commit changes in the staging (middle) area
   git add .
   git commit -m "Initial commit"
   
5) Pull the remote changes:
   git pull origin main --rebase
This command pulls the remote changes and applies your local changes on top of them (via rebase), which avoids unnecessary merge commits.

6) Push your changes after pulling:
   git push origin main
If there are any conflicts during the git pull step, Git will notify you, and you'll need to resolve them manually before proceeding with the push.

7) Cloning the repo in Rupak's local -
   git clone https://github.com/username/repository.git
   cd repo_name

8) Rupak will now create his own branch and clone this repo to his local.
   git checkout -b branch_name
   (git checkout -b rupak)

9)  

