import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))

experience = []
salary = []

for i in range(n):
    exp = int(input("Enter years of experience: "))
    sal = int(input("Enter salary: "))
    experience.append(exp)
    salary.append(sal)

plt.figure()
plt.plot(experience, salary)
plt.title("Experience vs Salary - Line Chart")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
