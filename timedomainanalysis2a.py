import numpy as np  # Imports the NumPy library for numerical calculations.
import matplotlib.pyplot as plt  # Imports Matplotlib for plotting and visualizations.

# Parameters
time_bins = 100  # Total number of time bins (each representing 1 second).
time = np.arange(0, time_bins, 1)  # Creates an array of time values from 0 to 99 seconds.
periodicity = 25  # Defines the period of the sinusoidal oscillation (25 seconds).
max_rate = 400  # Sets the maximum photon count rate (peak of the sinusoidal wave).
min_rate = 1  # Sets the minimum photon count rate (trough of the sinusoidal wave).

# Generate sinusoidal light curve
photon_count_rate = ((max_rate - min_rate) / 2) * np.sin((2 * np.pi / periodicity) * time) + ((max_rate + min_rate) / 2)
# ((max_rate - min_rate) / 2): Calculates the amplitude of the sinusoidal wave.
# np.sin((2 * np.pi / periodicity) * time): Creates a sinusoidal oscillation with a period of 25 seconds.
# ((max_rate + min_rate) / 2): Shifts the wave upward so the photon count oscillates around the midpoint of max_rate and min_rate.

# Plot the mock light curve
plt.figure(figsize=(10, 6))  # Creates a figure with a specified size (10x6 inches).
plt.plot(time, photon_count_rate, label='Mock X-ray Light Curve')  # Plots the sinusoidal photon count rate versus time.
plt.title('Mock X-ray Light Curve (Sinusoidal)')  # Adds a title to the plot.
plt.xlabel('Time (s)')  # Labels the x-axis as "Time (s)".
plt.ylabel('Photon Count Rate (counts/s)')  # Labels the y-axis as "Photon Count Rate (counts/s)".
plt.grid()  # Adds a grid to the plot for better visualization.
plt.legend()  # Displays a legend for the plot, using the specified label.
plt.show()  # Displays the plot.




