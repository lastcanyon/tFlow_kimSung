import tensorflow as tf

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.mul(a, b)

#이것은 무엇을 하는 것인가.. with..?
with tf.Session() as sess:
    print ("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    print ("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))
