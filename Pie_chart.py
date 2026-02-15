import matplotlib.pyplot as plt

n = int(input("Enter number of departments: "))

departments = []
count = []

for i in range(n):
    dept = input("Enter department name: ")
    num = int(input("Enter number of employees: "))
    departments.append(dept)
    count.append(num)

plt.figure()
plt.pie(count, labels=departments, autopct='%1.1f%%')
plt.title("Department Distribution - Pie Chart")
plt.show()
