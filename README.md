# Python-code-for-taking-attendance-marks-for-a-company
Python code for taking attendance marks for a company

In this code, we first connect to the company database using the sqlite3 module. We then create a table to store attendance marks if it doesn't already exist. Next, we display a list of employees for the user to choose from, and prompt them for the employee ID and attendance status (P for present, A for absent, L for late).

We then check if the employee exists in the database, and if so, record the attendance mark for that employee on the current date. Finally, we commit the changes to the database and close the connection.

Note that this is just a basic example, and there are many other features that could be added, such as error handling, input validation, and reporting tools to analyze attendance data over time(Asiri pathum)
