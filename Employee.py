import matplotlib.pyplot as plt

employees = ["Asha", "Ravi", "Kiran", "Meena", "Arjun"]
salary = [25000, 30000, 28000, 35000, 40000]

plt.figure()
plt.bar(employees, salary)
plt.title("Employee Salary - Bar Chart")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()
