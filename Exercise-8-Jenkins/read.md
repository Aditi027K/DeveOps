@'
# Exercise 8 – Jenkins CI Automation

## Objective

To create a Jenkins Freestyle project that retrieves source code from GitHub and executes a shell script.

## Project Structure

```text
Exercise-8-Jenkins/
├── hello-world.sh
└── read.md
Shell Script
The hello-world.sh script contains:
#!/bin/bash
echo "Hello, Jenkins!"

Jenkins Job
A Jenkins Freestyle project named HelloWorld is configured.
Source Code Management
The Jenkins job uses the GitHub DevOps repository and the branch branch.
Build Step
The build executes:
sh hello-world.sh

Expected Output
Hello, Jenkins!
Finished: SUCCESS

Result
The Jenkins job successfully retrieves the source code from GitHub and executes the shell script.
'@ | Out-File -Encoding utf8 read.md

### Step 5 — Check both files

Run:

```powershell
dir

You should see:
hello-world.sh
read.md

Then:
type read.md