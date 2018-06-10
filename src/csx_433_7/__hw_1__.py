import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

a = np.matrix([[1, 2, 3, 4], [5, 6, 7, 4], [5, 2, 5, 6]])

b = tf.reduce_prod(a, name="produce_a")

c = tf.reduce_sum(a, name="sum_a")

d = tf.reduce_mean(a, name="mean_a")

e = tf.add(a, b, name="sum_a_b")

f = tf.multiply(c, d, name="multiply_c_d")

g = tf.add(e, f, name="total_sum")

writer = tf.summary.FileWriter('./name_scope_2', graph=tf.get_default_graph())
writer.close()