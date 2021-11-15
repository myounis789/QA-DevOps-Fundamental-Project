# QA-DevOps-Fundamental-Project- Restaurant Reserver App:

This repository contains my deliverable for my QA devops fundamental project.

## Contents:

- [Project Brief](#Project-Brief)
- [App Design](#App-Design)
- [Risk Assessment](#Risk-Assessment)
- [The App](#The-App)
- [Known Issues](#Known-Issues)
- [Future Work](#Future-Work)

## Project Brief:

The brief for this project was to design and produce a CRUD application. The needs to execute the following functions:
CREATE
READ
UPDATE
DELETE

It needs to be connected to an SQL database with atleast one one-to-many database relationsip

Before I start, I planned out my project requirements:

![project requirements](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/projectrequirements.png)

## App Design:
Software flowcharts were designed to establish functionality for each usertype:

Customer Login Software Flowchart (including CRUD functionality):


![Flowchart](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/Customer%20software%20flowchart.png)  

Admin Login Software Flowchart (including CRUD functionality):


![AdminFlowchart](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/Admin%20software%20flowchart.png)  

The following ERD was produced:


![Current ERD](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/ERD%20Diagram.png.png)


## Risk Assessment:
The following risks were identified:
- Security breach as user accounts can be accessed if loginId leaked. Will use a random unique login Id generator to increase complexity of ID.
- user info is not hashed so developers can view all their personal records

# The App:
Here are some screenshots of my application running on the server:

homepage/welcome page


![home](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/welcome.png)  

customer landing page

![customerHome](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/customerHome.png) 

admin landing page

![adminHome](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/adminHome.png) 

managebookings

![manageBookings](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/bookinghistory.png) 

account details


![accontDetails](https://github.com/myounis789/QA-DevOps-Fundamental-Project/blob/main/Documentation/accountDetails.png) 
## Known Issues:

- Can't implement filter by name on admin homepage which would've been very useful
- Sometimes booking status doesn't update unless page is refreshed.
- 
## Future Work:

As a future development, I would add a logn feature with an encrypted password feature to be stored via hashing. This maks each LoginId customised to their own password and user doesn't need to remember a random id.
