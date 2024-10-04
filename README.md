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

--- Invite Rupak as collaborator. ---

7) Cloning the repo in Rupak's local -
   git clone https://github.com/username/repository.git
   cd repo_name

8) Rupak will now create his own branch and clone this repo to his local.
   git checkout -b branch_name
   (git checkout -b rupak)

9)  Switch to the rupak branch (if he isn't already on it):
   git checkout rupak

10) Add the changes to the staging area:
    git add .

11) Commit the changes with a descriptive message:
   git commit -m "Describe the changes made"

12) Push the changes to the remote rupak branch:
   git push origin rupak

13) Rupak clicked on compare and pull requests and sent it to me. I approved the pull request and checked the code changes.

14) I clicked on merge pull request.

15) Rupak can now see approved merge in his github.

16) Now I want to use this code so I need to pull it to my local.
    git checkout main
    git pull origin main

    
