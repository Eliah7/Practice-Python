"""Use NumPy arrays for large lists"""

import numpy as np
import tensorflow as tf

x = np.random.randint(1000,size=10000)
y = tf.Variable(5*(x**2) - 3*x + 15,name='y')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(y))
