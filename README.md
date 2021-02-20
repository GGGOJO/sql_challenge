# sql_challenge
This challenge required the following SQL activities in two parts:
  * Create an Entity Relationship Diagram (EDR) - Data Engineering or Modeling work
  * Conduct queries - Data Analysis work
  
## PART I: Create a Table Schema 
I was given six Employee-type csv files to examine:
    1. departments
    2. department employee
    3. department manager
    4. employees
    5. salaries
    6. titles

After review, I figured out the data types and the relationships (primary and foreign keys). I used the Quick Database Diagrams (Quick DBD) to create the data "blueprint". As the forthcoming analysis is based on the employees at the fictious company (Pewlett Hackard), I found out that the relationships were "One to One". The EDR output is in the GitHub and called "EDR_Data_Engineering_Schema".

## PART II: Run SQL Queries
In this part of the challenge, I needed to run queries across the six csv files. 

First, I created table shells for the data to be imported into. For each attribute, I identified the data type as well as made data required (i.e., NOT NULL). Taking care of which attributes within each entity (table) had primary keys, and referencing foreign keys to other entities. 

Second, I imported the csv files into the table using the 
```sql
COPY [Table Name] 
FROM '[Absolute Path to File]' 
DELIMITER '[Delimiter Character]' CSV [HEADER];
```
Once the data have been imported, I could run the queries (my solution's approach):
1.    List the following details of each employee: employee number, last name, first name, sex, and salary. *APPROACH: query from merge employees with salary tables.*

2.    List first name, last name, and hire date for employees who were hired in 1986. *APPROACH: query from employees table.*

3.    List the manager of each department with the following information: department number, department name, the manager’s employee number, last name, first name. *APPROACH: query from merging three tables department, dept_manager, employees.*

4.    List the department of each employee with the following information: employee number, last name, first name, and department name. *APPROACH: query from merge employees and departments.*


5.    List first name, last name, and sex for employees whose first name is “Hercules” and last names begin with “B.” *APPROACH: query from employees table.*

6.    List all employees in the Sales department, including their employee number, last name, first name, and department name. *APPROACH: query from department and employees.*


7.    List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name. *APPROACH: query from department and employees.*

8.    In descending order, list the frequency count of employee last names, i.e., how many employees share each last name. *APPROACH: group by and order desc from employees table.*

## Bonus Questions
Import SQL Data from Postgresql and conduct the following data analysis using Pandas in Jupyter Notebook:
1. Create a histogram to visualize the most common salary ranges for emmployees. 
2. Create a bar chart of average salary by title.

After diving into the data, what is the answer to this question? 

Q: Is the Pewlett Hackard Employee Data fake? 
A: Yes, it is.


