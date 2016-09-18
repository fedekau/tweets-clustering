# http://blog.altoros.com/using-k-means-clustering-in-tensorflow.html

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

points_n = 500
clusters_n = 10
iteration_n = 100

# Generate random data points (with uniform distribution) & assign them to a 2D tensor constant.
points = tf.constant(np.random.uniform(0, 10, (points_n, 2)))
# Choose randomly the initial centroids
centroids = tf.Variable(tf.slice(tf.random_shuffle(points), [0, 0], [clusters_n, -1]))

# want to do element-wise subtraction of points and centroids that are 2D tensors.
# Because tensors have different shape, let_s expend points and centroids into 3 dimensions,
# which allows us to use the broadcasting feature of subtraction operation.
points_expanded = tf.expand_dims(points, 0)
centroids_expanded = tf.expand_dims(centroids, 1)

# calculate distances between points & centroids and determine the cluster assignments.
distances = tf.reduce_sum(tf.square(tf.sub(points_expanded, centroids_expanded)), 2)
assignments = tf.argmin(distances, 0)

# We can compare each cluster with a cluster assignments vector,
# get points assigned to each cluster, and calculate mean values.
# These mean values are refined centroids,
# so let_s update the centroids variable with the new values.
means = []
for c in xrange(clusters_n):
	means.append(tf.reduce_mean(
		tf.gather(points,
		tf.reshape(
		tf.where(tf.equal(assignments, c)),[1,-1])
		),reduction_indices=[1]))

new_centroids = tf.concat(0, means)

update_centroids = tf.assign(centroids, new_centroids)
init = tf.initialize_all_variables()

# . For each iteration, we update the centroids & return their values along with the cluster assignments values.
with tf.Session() as sess:
	sess.run(init)
	for step in xrange(iteration_n):
		[_, centroid_values, points_values, assignment_values] = sess.run([update_centroids, centroids, points, assignments])

		print "centroids" + "\n", centroid_values

#  Display coordinates of the final centroids and a multi-colored scatter plot showing how the data points have been clustered.
plt.scatter(points_values[:, 0], points_values[:, 1], c=assignment_values, s=50, alpha=0.5)
plt.plot(centroid_values[:, 0], centroid_values[:, 1], 'kx', markersize=15)
plt.show()
