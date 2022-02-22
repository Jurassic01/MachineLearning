import time
import random
import numpy as numpy

def inputMatrix(rows, columns):
    MyMatrix=[]
    for i in range(rows):
        MyMatrix.append([])
        for j in range(columns):
             MyMatrix[i].append(random.randint(-44, 44))                
    return MyMatrix

size = int(input("size: "))

MyMatrix1 = inputMatrix(size, size)
MyMatrix1NumPy = numpy.array(MyMatrix1)

MyMatrix2 = inputMatrix(size, size)
MyMatrix2NumPy = numpy.array(MyMatrix2)

#Numpy method
sratTimeNumMethod = time.time()
results = numpy.dot(MyMatrix1NumPy, MyMatrix2NumPy)
timeNumpy = time.time() - sratTimeNumMethod

#Custom method
ResultMatrix = inputMatrix(size, size)
sratTimeMyMethod = time.time()
for i in range(len(MyMatrix1)):
   for j in range(len(MyMatrix2[0])):
       for k in range(len(MyMatrix2)):
           ResultMatrix[i][j] += MyMatrix1[i][k] * MyMatrix2[k][j]
timeLoop = time.time() - sratTimeMyMethod


print("Time custom method: {:.5f}s ".format(timeLoop))
print("Time Numpy method: {:.5f}s ".format(timeNumpy))