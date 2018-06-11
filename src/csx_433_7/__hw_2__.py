# Name, Email and GitHub URL
"""
Name : Sanatan Das
Email : sanatanonline@gmail.com
GitHub URL : https://github.com/sanatanonline/compscix-433-assignments/blob/master/src/csx_433_7/__hw_2__.py

"""

# Import tensorflow library and reference it as 'tf'
import tensorflow as tf
# Import matplotlib.pyploy library and reference as 'plt'
import matplotlib.pyplot as plt
import os

# Please ignore the below line of code.
# In pycharm the following error occurs if tensor flow 1.8 version.
# Error: Your CPU supports instructions
# that this TensorFlow binary was not compiled to use: AVX2 FMA
# This line of code is a fix for it.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Clear cache for default graph
tf.reset_default_graph()

# Scope of input section
with tf.name_scope("Input_placeholder"):
    # Define placeholder array of type float32
    A = tf.placeholder("float32", shape=None, name="Input_placeholder_a")
    # Create normally distributed tensor of 100 numbers
    # Mean = 1 and Standard Deviation = 2
    a_tensor = tf.random_normal(shape=(100,), mean=1.0, stddev=2.0)

# Scope of middle section
with tf.name_scope("Middle_section"):
    # Reduce prod operation and assign it to b
    b = tf.reduce_prod(A, name="b_prod")
    # Reduce mean operation and assign it to c
    c = tf.reduce_mean(A, name="c_mean")
    # Reduce sum operation and assign it to d
    d = tf.reduce_sum(A, name="d_sum")
    # Add b and c and assign it to d
    e = tf.add(c, b, name="e_add")

# Scope of final section
with tf.name_scope("Final_node"):
    # Multiply d and e and assign it to final node f
    f = tf.multiply(d, e, name="f_mul")

# Start the session using the default graph
with tf.Session() as sess:
    # Evaluate tensor of random 100 numbers. Output is numpy array
    a = a_tensor.eval()
    # Run the session for final output
    sess.run(f, feed_dict={A: a})

sess.graph.as_graph_def()
# Write the graph to 'hw2_graph' directory
writer = tf.summary.FileWriter('./hw2_graph', sess.graph)
# Close the writer
writer.close()
# Close the tensor flow session
sess.close()

# Plot a histogram for the input array
plt.hist(a, bins=25)
# Set the title of the diagram
plt.title("Histogram of Normal Distribution")
# X-axis label
plt.xlabel("Values")
# Y-axis label
plt.ylabel("Frequency")
# Show the plot
plt.show()
