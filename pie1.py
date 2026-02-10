import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5, 6, 7]

plt.pie(experience, labels=experience, autopct='%1.1f%%')
plt.title("Pie Chart: Experience Distribution")
plt.show()
