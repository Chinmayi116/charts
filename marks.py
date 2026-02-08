import matplotlib.pyplot as plt

# Sample data: Marks of students
marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
         85, 90, 95, 88, 78, 68, 58, 48, 38, 72]

# Create Histogram
plt.figure()
plt.hist(marks, bins=7)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Histogram of Students' Marks")
plt.show()
