import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()

a = 92

print(type(a))

a = tf.convert_to_tensor(a, dtype=tf.float16)

print(type(a))

b = tf.constant(92)

print(type(a))

print(a == b)

sess.close()



