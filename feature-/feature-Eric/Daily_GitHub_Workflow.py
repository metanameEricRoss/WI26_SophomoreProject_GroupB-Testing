# Daily GitHub Workflow Script
import subprocess
import time

# slow the output for readability
def pause():
    time.sleep(0.4)

# Run a shell command and print result
def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

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
    bailout = input("Do you want to proceed? (y/n): ")
    if bailout.lower() != 'y':
        print("Exiting script.")
        pause()
        exit() # Exit the script if user does not want to proceed

    # Get user input for mode and branch name
    try:
        mode = int(input("Enter mode (0,1); ('0' = start, '1' = end): "))
    except ValueError:
        print("Invalid input. Please enter 0 or 1.")
        pause()
        continue   # changed: pass --> continue.

    feature_branch = input("Enter your feature branch name(example- 'feature-Eric'): ")

    # NEW: Validate branch exists before continuing
    check_branch = subprocess.run(
        f"git rev-parse --verify {feature_branch}",
        shell=True,
        capture_output=True,
        text=True
    )
    if check_branch.returncode != 0:
        print(f"Error: Branch '{feature_branch}' does not exist.")
        pause()
        print("Restarting...\n")
        continue  # restart input loop

    # Confirm inputs if 'n' restart loop
    confirm = input(f"You selected mode {mode} for branch '{feature_branch}'. Confirm? (y/n): ")

    if confirm.lower() == 'y':
        break  # Exit the loop and continue the script
    else:

        print("Restarting...")
        pause()


#=============================================================
#====================    mode loop      ======================
#=============================================================

              # Mode == 0; Start of day: update main and create branch
if mode == 0: #=============================================================
    print("\nStarting your day...")
    pause()
    print('run_command("git checkout main")')
    run_command("git checkout main")
    pause()
    print('run_command("git pull")')
    run_command("git pull")
    pause()
    print(f'Creating and switching to branch: {feature_branch}')
    run_command(f"git checkout {feature_branch}") #-b creates a new branch. *Removed
    pause()
    print("\nBranch ready.")




                # Mode == 1; End of day: commit and push work
elif mode == 1: #=============================================================
    print(f"\nSaving work to branch ** {feature_branch} **")
    pause()
    print("{'.' = all; 'my-feature.py' = specific name.}")
    fileselect = input("What files do you want to add:  ")

    if fileselect == '.':
        run_command("git add .")
    else:
        print(f"Adding file: {fileselect}")
        run_command(f"git add {fileselect}")
    pause()
    commit_msg = input("Enter commit message: ")

    print("Are you sure you want to commit?")
    pause()
    check = input(f"{commit_msg} -- (y/n): ")

    if check.lower() != 'y':
        print("Commit cancelled.")
    else:
        print("\nCommitting and pushing...")
        pause()
        print(f"Committing with message: {commit_msg}")
        run_command(f"git commit -m '{commit_msg}'")
        pause()
        print(f"Pushing to branch: {feature_branch}")
        run_command(f"git push origin {feature_branch}")
        pause()
        print("\nWork pushed.")

# Invalid mode
else: #=============================================================
    print("Invalid mode. Use 0 or 1.")
