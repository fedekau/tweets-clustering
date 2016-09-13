import date_clustering as cl
import numpy as np
import matplotlib.pyplot as plt


top_right = np.random.rand(40,2) + [0, 0]
top_left = np.random.rand(40,2) + [-1, 1]
bottom_left = np.random.rand(40,2) + [0, 0]
bottom_right = np.random.rand(40,2) + [1, -1]

vectors = np.concatenate((top_right, top_left, bottom_left, bottom_right))

res = cl.TFKMeansCluster(vectors, 4)

center1 = res[0][0]
center2 = res[0][1]
center3 = res[0][2]
center4 = res[0][3]


array_1_x = []
array_1_y = []
array_2_x = []
array_2_y = []
array_3_x = []
array_3_y = []
array_4_x = []
array_4_y = []

for i in range(len(top_right)):
	array_1_x.append(top_right[i][0])
	array_1_y.append(top_right[i][1])

	array_2_x.append(top_left[i][0])
	array_2_y.append(top_left[i][1])

	array_3_x.append(bottom_left[i][0])
	array_3_y.append(bottom_left[i][1])

	array_4_x.append(bottom_right[i][0])
	array_4_y.append(bottom_right[i][1])


for i in range(len(top_left)):
	plt.plot(array_1_x, array_1_y, 'ro')
	plt.plot(array_2_x, array_2_y, 'go')
	plt.plot(array_3_x, array_3_y, 'co')
	plt.plot(array_4_x, array_4_y, 'ko')

plt.plot(center1[0], center1[1], 'mx')
plt.plot(center2[0], center2[1], 'mx')
plt.plot(center3[0], center3[1], 'mx')
plt.plot(center4[0], center4[1], 'mx')

plt.show()
