import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5]
salary = [20000, 25000, 30000, 35000, 40000]

plt.figure()
plt.plot(experience, salary)
plt.title("Experience vs Salary - Line Chart")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
