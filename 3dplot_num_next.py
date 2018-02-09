'''
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
zVals_15_full = []
zVals_16_full= []
aVals_15_full = []
bVals_15_full = []
aVals_16_full = []
bVals_16_full = []

num = 20 

print("k_of_" + sys.argv[1]+"next" + ".csv")

#print("num")
#print(num)

 

   
i = 0
zVals_15 = []
zVals_16 = []
aVals_15 = []
bVals_15 = []
aVals_16 = []
bVals_16 = []
with open("k_of_" + sys.argv[1] + "next" + ".csv", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')

    for row in spamreader:	
        #print("w-0")
        if(i != 0):
           #print("w-1")
           if(row[2] != ' '):
              #print("w-2")
              aVals_15.append(float(row[0]))  
              bVals_15.append(float(row[1]))  
              que = 0
              for k in range(num):
                 if(row[2+k] != ' '):
                     que+=1
              zVals_15.append(que)
           #print(k)
           #print(row)	
           if(row[2+num] != ' '):
              aVals_16.append(float(row[0]))  
              bVals_16.append(float(row[1]))  
              que = 0
              for k in range(num):
                 if(row[2+k+num] != ' '):
                     que+=1
              zVals_16.append(que)
        i+=1
   
zVals_15_full.append(zVals_15)
zVals_16_full.append(zVals_16)
aVals_15_full.append(aVals_15)
bVals_15_full.append(bVals_15)
aVals_16_full.append(aVals_16)
bVals_16_full.append(bVals_16)
		

color_array = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w', '#33ff4c', '#ff33f7', '#fbff33', '#ff9733', '#c333ff', '#33ffa3', '#9bff33', '#33ffff','#ff3387', '#1b4f38', '#e1a9a9', '#a9e1a9', '#d0e131', '#bbe131', '#31d0e1', '#e131de']
marker_array = ['.', '.','.','.','.','.','.','.',      'd', 'd','d','d','d','d','d','d',      's', 's', 's', 's', 's', 's', 's', 's']

#print("test1")

xs = np.array(aVals_15_full[0])
ys = np.array(bVals_15_full[0])
zs = np.array(zVals_15_full[0])
''' 
print(k)

print("xs")
print(xs)

print("ys")
print(ys)

print("zs")
print(zs)
'''

ax.scatter(xs, ys, zs, c=color_array[0], marker=marker_array[0])

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('roots (15)')

plt.show()

fig = plt.figure()
ae = fig.add_subplot(111, projection='3d')


xs = np.array(aVals_16_full[0])
ys = np.array(bVals_16_full[0])
zs = np.array(zVals_16_full[0])

'''
print(k)

print("xs")
print(xs)

print("ys")
print(ys)

print("zs")
print(zs)
'''


ae.scatter(xs, ys, zs, c=color_array[0], marker=marker_array[0])

ae.set_xlabel('a')
ae.set_ylabel('b')
ae.set_zlabel('roots (16)')

plt.show()
