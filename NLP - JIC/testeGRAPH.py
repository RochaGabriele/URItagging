import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import pyplot
import pylab
from mpl_toolkits.mplot3d import Axes3D

fig = pylab.figure()
ax = Axes3D(fig)

X = np.random.randint(25,50,(25,3))
Y = np.random.randint(60,85,(25,3))
W = np.random.randint(100,120,(25,3))

Z = np.vstack((X,Y, W))
# convert to np.float32
Z = np.float32(Z)


# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,3,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now separate the data, Note the flatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
C = Z[label.ravel()==2]
listA = []
listA.append(A)
listA.append(B)
listA.append(C)

seq_x = []
seq_y = []
seq_z = []

for i, item in enumerate(listA):
    for j in item:
        seq_x.append(j[0])
        seq_y.append(j[1])
        seq_z.append(j[2])
    if i == 0:
        ax.scatter(seq_x, seq_y, seq_z, c = 'r')
    if i == 1:
        ax.scatter(seq_x, seq_y, seq_z, c = 'g')
    if i == 2:
        ax.scatter(seq_x, seq_y, seq_z, c = 'b')
    
    seq_x = []
    seq_y = []
    seq_z = []
pyplot.show()


# Plot the data
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(C[:,0],C[:,1],c = 'g')

plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()
