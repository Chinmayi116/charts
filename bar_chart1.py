import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5, 6, 7]
salary = [20000, 25000, 30000, 38000, 45000, 52000, 60000]

plt.bar(experience, salary)
plt.xlabel("Work Experience (Years)")
plt.ylabel("Salary")
plt.title("Bar Chart: Experience vs Salary")
plt.show()
