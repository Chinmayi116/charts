import matplotlib.pyplot as plt

# Sample data: Heights of school students (in cm)
heights = [120, 130, 125, 140, 135, 150, 145, 155, 160, 165,
           170, 158, 162, 168, 172, 175, 180, 138, 142, 148]

# Create Histogram
plt.figure()
plt.hist(heights, bins=6)
plt.xlabel("Height (cm)")
plt.ylabel("Number of Students")
plt.title("Histogram of School Students' Heights")
plt.show()
