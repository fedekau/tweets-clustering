import tensorflow as tf

def print_tf( v ):
	tf.initialize_all_variables()
	with tf.Session as sess:
		sess.run(v)
