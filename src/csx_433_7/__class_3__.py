import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with tf.name_scope("Scope_A"):
    a = tf.add(1, 2, name="A_add")
    b = tf.multiply(a, 3, name="A_mul")

with tf.name_scope("Scope_B"):
    c = tf.add(4, 5, name="B_add")
    d = tf.multiply(c, 3, name="B_mul")

e = tf.add(b, d, name="output")

writer = tf.summary.FileWriter('./name_scope_1', graph=tf.get_default_graph())
writer.close()

