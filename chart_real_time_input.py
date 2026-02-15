import matplotlib.pyplot as plt

n = int(input("Enter number of employees: "))

employees = []
salary = []

for i in range(n):
    name = input("Enter employee name: ")
    sal = int(input("Enter salary: "))
    employees.append(name)
    salary.append(sal)

plt.figure()
plt.bar(employees, salary)
plt.title("Employee Salary - Bar Chart")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()
