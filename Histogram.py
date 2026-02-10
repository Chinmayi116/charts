import matplotlib.pyplot as plt

salary = [20000, 25000, 30000, 38000, 45000, 52000, 60000]

plt.hist(salary)
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Histogram: Salary Distribution")
plt.show()
