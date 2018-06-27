"""
Name        : Sanatan Das
Email       : sanatanonline@gmail.com
GitHub URL  : https://github.com/sanatanonline/compscix-433-assignments/blob/master/src/csx_433_3
Assignment  : Midterm

"""

# Import numpy library and reference as 'np'
import numpy as np
# Import the pylab library and reference as 'plb'
import pylab as plb

# 1. An array with 12 elements beginning from number 5, containing consecutive odd numbers
A = np.arange(5, 28, 2)
print(A)

# 2. Compute the simple moving average of an array(SMA),
#    using an adjustable window using a function.
#    The function calculating the SMAof the array must take two input arguments:
#    - the array(A)
#    - a window width with a default value 2

# 3. After every SMA is collected (as array) calculate its current cumulative moving average (CMA)


# Simple moving average function
def func_simple_moving_average(input_arr, win=2):  # window width default value is 2
    moving_average = np.cumsum(input_arr, dtype=float)
    moving_average[win:] = moving_average[win:] - moving_average[:-win]
    cumulative_moving_average = moving_average[win-1:]/win
    return cumulative_moving_average


# 4. Make two function calls to the SMA:
#   1st call: pass the array A only. Save this SMA to B
#   2nd call: specifying a window width = 4. Save this SMA to C

# 1st function call with default window (which is 2)
B = func_simple_moving_average(A)

# 2nd function call with window size of 4
C = func_simple_moving_average(A, 4)


# 5. Print the results from the two calls made above using short description of the data

# Print the original array
print('The original array is: ', A)

# Print SMA result with default window (which is 2)
print('Moving average result is B:', B)
# Print the window width for B
print('Window width for B:', 12-len(B) + 1)

# Print SMA result with window size of 4
print('Moving average result for C:', C)
# Print the window width for C
print('Window width for C:', 12-len(C) + 1)


# 6. Plot
#   - The sin functions for array B and C
#   - Show the grid, legend

# Create a plot
plb.figure(figsize=(10, 6), dpi=120)

# Create the subplot for sinB function
plb.subplot(2, 1, 1)
# Add title
plb.title('Plot of sinB')
# Plot the graph with color, linewidth, linestyle, label
plb.plot(B, plb.sin(B), color='blue', linewidth=1.5, linestyle='-', label='sinB')
plb.ylim(plb.sin(B).min(), plb.sin(B).max())
plb.xlim(B.min(), B.max())
# Add grid
plb.grid()
# Add Y-axis label
plb.ylabel('Y-Axis')
# Add legend
plb.legend(loc='upper right')

# Create the subplot for sinC function
plb.subplot(2, 1, 2)
# Add title
plb.title('Plot of sinC')
# Plot the graph with color, linewidth, linestyle, label
plb.plot(C, plb.sin(C), color='red', linewidth=1.2, linestyle='-.', label='sinC')
plb.ylim(plb.sin(C).min(), plb.sin(C).max())
plb.xlim(C.min(), C.max())
# Add grid
plb.grid()
# Add Y-axis label
plb.ylabel('Y-Axis')
# Add X-axis label. One label for both the subplots
plb.xlabel('X-Axis')
# Add legend
plb.legend(loc='upper right')

# Show the plot
plb.show()
