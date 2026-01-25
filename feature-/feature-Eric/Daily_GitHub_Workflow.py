# Daily GitHub Workflow Script

'''
note to self:

I need to impliment a test feature, 
possibly on a featrure-test branch,
    to validate user inputs function correctly,
    also find a method to prevent accidental data loss.
    and improper branch handling while also making it possible to create a new branch.

    - instead of 0, 1 mode` input,
        use descriptive text input like "start" or "end".
        include more functions later on.

    - modularlize the code into functions for better readability and maintainability.        

'''

import subprocess
import time

# slow the output for readability
def pause():
    time.sleep(0.4)

# Run a shell command and print result
def run_command(command):
    result = subprocess.run(
        command, 
        shell=True, 
        capture_output=True, 
        text=True)

    if result.returncode == 0:
        print(f"Success: {command}")
    else:
        print(f"Error: {command}")
        print(result.stderr)  # Print error message

#=============================================================
#====================   User Input      ======================
#=============================================================

            # Mode 0 = start of day, Mode 1 = end of day
while True: #=============================================================
    bailout = input("Do you want to proceed? (y/n):  ")
    if bailout.lower() != 'y':
        print("\nExiting script...")
        pause()
        exit() # Exit the script if user does not want to proceed

    # Get user input for mode and branch name
    try:
        mode = int(input("('0' = start, '1' = end) \n --> Enter mode (0,1): "))
    except ValueError:
        print("Invalid input! \n Please enter 0 or 1.")
        pause()
        continue   # changed: pass --> continue.

    feature_branch = input("Enter your feature branch name(example- 'feature-Eric'): ")

    if feature_branch == 'EXIT': 
        print("\nExiting script...")
        pause()
        exit()

    # NEW: Validate branch exists before continuing
    check_branch = subprocess.run(
                                                    #The primary purpose of this command is to allow calling programs... 
                                                    #  to distinguish between them. There are a few other operation modes 
                                                    #   that have nothing to do with the above "help parse command line options"
        f"git rev-parse --verify {feature_branch}",     # '--verify' 
        shell=True,                                     # that exactly one parameter is provided,  that can be used to access the object database.
        capture_output=True,                            #   and that it can be turned into a raw 20-byte SHA-1 hash.
        text=True                                       #     If so, emit it to the standard output; otherwise, error out. - Git Documentation
    )
    # try except BLOCK ?
    if check_branch.returncode != 0: # Error code means branch does not exist
        print(f"Error: Branch '{feature_branch}' does not exist.")
        pause()
        new_branch = input("Do you want to create it? (y/n): ")
        if new_branch.lower() == 'y':
            print(f"Creating branch '{feature_branch}'...")
            run_command(f"git checkout -b {feature_branch}")
            pause()
        else:
            print("Restarting...\n")
            continue  # restart input loop

    else :
        # Confirm inputs if 'n' restart loop
        confirm = input(f"\n\nMode: {mode} \nBranch: '{feature_branch}'.\n\t--> Confirm? (y/n): ")

        if confirm.lower() == 'y':
            break  # Exit the loop and continue the script

        elif confirm == 'EXIT':
            print("\nExiting script...")
            pause()
            exit()
        else:
            pause()
            print("Restarting...")
            pause()


#=============================================================
#====================    mode loop      ======================
#=============================================================


              # Mode == 0; Start: Always pull from main 
              #                     and move to feature branch
#=============================================================
if mode == 0: 
    print("\n--> Starting...\n\n")
    pause()

    print('run_command("git checkout main")\n')
    run_command("git checkout main")

    pause()
    print('run_command("git pull")\n')
    run_command("git pull")

    pause()
    print(f'Creating and switching to branch: {feature_branch} \n')
    run_command(f"git checkout {feature_branch}") #-b creates a new branch. 

    pause()
    print(f'Pulling latest changes from {feature_branch}\n')
    run_command(f"git pull origin {feature_branch}") # added feature- branch pull

    pause()
    print("\n\n--> Branch ready.")


                # Mode == 1; End: commit and push work 
                #                       to feature-branch.
#=============================================================
elif mode == 1: 
    print(f"\nSaving work to ** {feature_branch} **")
    pause()
    fileselect = input("What files do you want to stage ('.' = all):  ")

    if fileselect == '.':
        run_command("git add .")
    else:
        print(f"Adding file: {fileselect}")
        pause()
        run_command(f"git add {fileselect}")
        pause()

    # Get commit message with confirm before committing
    commit_msg = input("Enter commit message: ")
    print("Are you sure you want to commit?\n>\n>")
    pause()
    check = input(f">>> {commit_msg} -- (y/n): ")

    if check.lower() != 'y':
        print("\nCommit cancelled.")
    else:
        print(f"\nCommitting with message: {commit_msg}")
        run_command(f"git commit -m '{commit_msg}'")
        pause()

        print(f"\nPushing to branch: {feature_branch}")
        run_command(f"git push origin {feature_branch}")
        pause()

        print(f"\nPushed to {feature_branch}.")

    # Invalid input
#=============================================================
else: 
    print("Invalid mode. Use 0 or 1.")
    pause()
