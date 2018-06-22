import tensorflow as tf

v = tf.random_normal([8], mean=-1, stddev=2)

sess = tf.Session()

print(sess.run(v))

