"""
Name : Sanatan Das
Email : sanatanonline@gmail.com
GitHub URL : https://github.com/sanatanonline/compscix-433-assignments/blob/master/src/csx_433_7/sanatan_das_midterm.py
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

# Take input length for vector size and convert to int
input_vector_length = int(input('Enter the length of your random vector:'))
# Take input length for vector size and convert to int
input_window_width = int(input('Enter the length of the window width:'))

# Create the graph
graph = tf.Graph()

with graph.as_default():
    with tf.name_scope("Variables"):
        # Variable to keep track of how many times the graph has been run
        global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name="global_step")

    with tf.name_scope("Input_section"):
        # Create input placeholder- takes in a Vector
        a = tf.placeholder(tf.float32, shape=[None], name="input_placeholder_a")

    with tf.name_scope("SMA_section"):
        # Compute the simple moving average
        cumulative_sum = tf.cumsum(a)  # Calculate sum
        simple_average_array = tf.div(cumulative_sum, input_window_width)  # Divide by window size
        output = tf.reduce_mean(simple_average_array, name="output")  # Calculate mean

    with tf.name_scope("SMA_summary"):
        # Increment the step every time by 1
        increment_step = global_step.assign_add(1)
        # Creates summaries for the output node
        tf.summary.scalar("SMA", output)
        # Initialization Op
        init = tf.global_variables_initializer()
        # Merge all summaries into one Operation
        merged_summaries = tf.summary.merge_all()

    # Run the tf session
    sess = tf.Session(graph=graph)
    print("graph execution started!")
    # Write the graph
    writer = tf.summary.FileWriter('./midterm_graph', graph)
    sess.run(init)
    # Run the graph for for 8 times
    for i in range(8):
        v = np.random.normal(loc=1, scale=2, size=input_vector_length)
        feed_dict = {a: v}
        _, step, summary = sess.run([output, increment_step, merged_summaries], feed_dict=feed_dict)
        writer.add_summary(summary, global_step=step)
    print("graph execution completed!")
