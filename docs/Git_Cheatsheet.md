# GitHub Helper. 

## Starting Out 

### Step 1: Clone the Repo
git clone https://github.com/EricRoss/WI26_SophomoreProject_GroupB-Testing.git

### Step 2: Create a Branch (your workspace.)
```
git checkout -b feature-yourname
```
- **-b**: makes a branch and not a repository.
- **pwd**, (Print Working Directory)
> **ALWAYS!** branch from main.

```
git checkout main 
git pull
git checkout -b feature-yourname
```

<img width="997" height="297" alt="image" src="https://github.com/user-attachments/assets/764e1b97-28e1-4c72-ad54-f3f282aa5e10" />
<br>

### Step 3: Make Changes
- Edit files
- Test locally

### Step 4: Commit Your Work
```
git add .
git commit -m "FEATURE: add login form"
```
### Step 5: Push to GitHub
```
git push origin feature-<yourname>
```
<img width="1215" height="733" alt="image" src="https://github.com/user-attachments/assets/f4c95353-0698-49a7-b175-efcfc5782e00" />

### Step 6: Open a Pull Request
Go to GitHub → Compare & Pull Request → Assign reviewer
>> 1. Go to Github
>> 2. Open a Pull Request
>> 3. Add a clear title and description.
>> 4. Assign Reviewer
>> 5. Wait for Approval
<br>

## Basic Terms
- **Repository (repo)** = your project folder on GitHub
- **Branch** = a separate workspace to test or build features
- **Commit** = a saved change with a message
- **Pull Request (PR)** = a formal request to merge changes into the main project

## Normal practice for maintaining a clean REPO
```
git Checkout main               #ALWAYS pull from main!!
git pull                        #gives the latest version of the main branch (whole repo)
git checkout feature-yourname   #Move to your branch.
git merge main                  #Brings your branch up to date with the changes made to main. 

git status   # what changed?
```



