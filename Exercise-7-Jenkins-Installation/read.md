\# Exercise 7 – Introduction to Continuous Integration (CI) and Jenkins Installation



\## Objective



To understand the concept of Continuous Integration (CI) and install Jenkins using Docker.



\## What is Continuous Integration?



Continuous Integration is a development practice where developers frequently integrate their code changes into a shared repository.



The main goal is to detect and fix errors early, improve software quality, and accelerate software delivery.



\## Key Features of CI



\- Frequent code integration

\- Automated builds

\- Automated testing

\- Immediate feedback



\## Benefits of CI



\- Early bug detection

\- Improved collaboration

\- Faster development cycles

\- High-quality code



\## How CI Works



1\. Developer writes code and pushes changes to Git.

2\. CI server detects the changes.

3\. Automated build is performed.

4\. Automated tests are executed.

5\. Results are communicated to the developer.



\## What is Jenkins?



Jenkins is an open-source automation server used to build, test, and deploy software. It supports Continuous Integration (CI) and Continuous Delivery (CD).



\## Key Jenkins Concepts



\- \*\*Job/Project:\*\* A task executed by Jenkins.

\- \*\*Build:\*\* Process of compiling and packaging code.

\- \*\*Pipeline:\*\* A sequence of steps used to build, test, and deploy an application.

\- \*\*Plugins:\*\* Extend Jenkins functionality.

\- \*\*Nodes:\*\* Machines where Jenkins jobs are executed.



\## Jenkins Installation Using Docker



Jenkins was installed using Docker with the following command:



```bash

docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
enkins Access

Jenkins was accessed through:

http://localhost:8080/



The initial administrator password was obtained from the Jenkins container during the initial setup.

Result

Jenkins was successfully installed using Docker and accessed through the web browser. The Jenkins dashboard was successfully opened and the installation was completed.



Then \*\*save the file\*\* and close Notepad.



\### STEP 3



After saving, come back to PowerShell and run:



```powershell

dir

