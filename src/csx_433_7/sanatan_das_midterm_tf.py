"""
Name : Sanatan Das
Email : sanatanonline@gmail.com
GitHub URL : https://github.com/sanatanonline/compscix-433-assignments/blob/master/src/csx_433_7/sanatan_das_midterm_tf.py
Assignment : Midterm

"""

# Import tensorflow library and reference it as 'tf'
import tensorflow as tf
# Import numpy library and reference it as 'np'
import numpy as np

import os

# Please ignore the below line of code.
# In pycharm the following error occurs if tensor flow 1.8 version.
# Error: Your CPU supports instructions
# that this TensorFlow binary was not compiled to use: AVX2 FMA
# This line of code is a fix for it.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Compute the SMA of a dynamic input using TensorFlow graph

# Clear cache for default graph
tf.reset_default_graph()

# 1. Use user input to define the length of your vector	and	the	window width

# Take input length for vector size and convert to int
input_vector_length = int(input('Enter the length of your random vector:'))
# Take input length for vector size and convert to int8
input_window_width = int(input('Enter the length of the window width:'))

with tf.name_scope("variables"):
    # Variable to keep track of how many times the graph has been run
    global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name="global_step")
    # Variable that keeps track of the sum of all output values over time:
    total_output = tf.Variable(0.0, dtype=tf.float32, trainable=False, name="total_output")

# Scope of input section
with tf.name_scope("input"):
    # Define placeholder array of type int32
    input_vector = tf.placeholder(tf.float32, shape=None, name="input_vector")
    # Define a placeholder for int window size
    input_window = tf.placeholder(tf.int32, shape=None, name="window_size")

# Scope of SMA section
with tf.name_scope("SMA_section"):
    output = tf.reduce_mean(input_vector, name="input_vector_mean")


# Summary Operations
with tf.name_scope("SMA_summary"):
    # Increments the total_output Variable by the latest output
    update_total = total_output.assign_add(output)
    # Increments the above `global_step` Variable, should be run whenever the graph is run
    increment_step = global_step.assign_add(1)
    # Creates summaries for output node
    # Creates summaries for output node
    tf.summary.scalar("output_summary", output)
    tf.summary.scalar("total_summary", update_total)
    # Initialization Op
    init = tf.initialize_all_variables()
    # Merge all summaries into one Operation
    merged_summaries = tf.summary.merge_all()


# Start the session using the default graph
with tf.Session() as sess:
    sess.run(init)
    v = np.random.normal(1, 2, input_vector_length)
    # Run the session for final output
    sess.run(output, feed_dict={input_vector: v, input_window: input_window_width})

sess.graph.as_graph_def()
# Write the graph to 'hw2_graph' directory
writer = tf.summary.FileWriter('./midterm_graph', sess.graph)
# Close the writer
writer.close()
# Close the tensor flow session
sess.close()



