
--TASK 1

SELECT DISTINCT job_id as positions FROM employees;

--TASK 2

SELECT AVG(SALARY) as avarage_salary, COUNT(first_name) as quantity FROM employees WHERE DEPARTMENT_ID = 90;


--TASK 3

SELECT JOB_ID AS direction, count(EMPLOYEE_ID) as quantity
FROM employees
GROUP BY JOB_ID order by QUANTITY;

--TASK 4

SELECT first_name, last_name, department_id FROM employees;

--TASK 5

SELECT first_name, last_name, job_id, department_id
FROM employees
JOIN departments USING (department_id)
JOIN locations USING (location_id)
WHERE city = 'London';
