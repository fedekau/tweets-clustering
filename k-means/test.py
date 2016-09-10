import date_clustering as cl
import numpy as np
import matplotlib.pyplot as plt


c1 = np.random.rand(20,2)
c_1 = np.random.rand(20,2) - 4
c2 = np.random.rand(20,2) + 10
c_2 = np.random.rand(20,2) - 10

vectors = np.concatenate((c1, c_1, c2, c_2))

res = cl.TFKMeansCluster(vectors, 4)

center1 = res[0][0]
center2 = res[0][1]
center3 = res[0][2]
center4 = res[0][3]

plt.plot(center1[0], center1[1], 'rx')
plt.plot(center2[0], center2[1], 'gx')
plt.plot(center3[0], center3[1], 'bx')
plt.plot(center4[0], center4[1], 'yx')

plt.plot(c1, 'ro')
plt.plot(c_1, 'go')
plt.plot(c2, 'bo')
plt.plot(c_2, 'yo')

plt.show()
