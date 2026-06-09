git add somefile.py # add a file to the staging area

git add -p # go through each change and decide whether to stage it or not

git commit -m "added somefile" # create a commit with the changes in the staging area

git commit -am "bunch of stuff" # add and commit in one step (only works for modified files, not new files)

git push # push to the remote

git pull # pull from the remote

git diff # see unstaged changes (I think if you only have staged changes this will show them? I forget)

git diff --staged # show staged changes

git log # show commit history

git status
