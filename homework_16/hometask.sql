
--TASK 1
SELECT * FROM employees ORDER BY FIRST_NAME;

--TASK 2
SELECT first_name, last_name, salary, salary * 0.15 as tax FROM employees;

--TASK 3
SELECT SUM(salary) as sum_salary FROM employees;

--TASK 4
SELECT MIN(salary) as min_salary FROM employees;
SELECT MAX(salary) as max_salary FROM employees;


-- TASK 5
SELECT COUNT(FIRST_NAME) as quantity, AVG(SALARY) as avarage_salary FROM employees;