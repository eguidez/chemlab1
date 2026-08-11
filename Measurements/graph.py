# This code produces the bar graph for the measurement lab.
import matplotlib.pyplot as plt
import numpy as np

# Four measurements
measurements = [0.884, 0.932, 1.152, 1.122]

# Labels for the measurements
labels = ["Measurement 1", "Measurement 2", "Measurement 3", "Measurement 4"]

#  Calculate average
average = sum(measurements) / len(measurements)

#Calculate standard deviation
standard_deviation = np.std(measurements, ddof=1)

# Reference density
ref_dens = 1.00

# Add average line
plt.axhline(
    y=average,
    color="red",
    linestyle="--",
    label=f"Average = {average:.2f} g/mL ± {standard_deviation:.2f} g/mL"
)
# Add true value line
plt.axhline(
    y=ref_dens,
    color="purple",
    linestyle="-",
    label=f"Reference density = {ref_dens:.2f} g/mL"
)
# Create bar graph
plt.bar(labels, measurements,yerr=standard_deviation,capsize=5)

# Add labels and title
plt.xlabel("Measurement")
plt.ylabel("Density (g/mL)")
plt.title("Density of water at 25°C obtained with the graduate cylinder")

# Display the values above each bar
for i, value in enumerate(measurements):
    plt.text(i, value + 0.01, str(value), ha="right")

print(f"Average = {average:.2f} g/mL")
print(f"Standard deviation = {standard_deviation:.2f} g/mL")

plt.legend(fontsize=8)
plt.show()

