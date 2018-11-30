# NumPy Analysis
# 
#author: Maurício Silva Soares
#
# Analysis of NumPy library in transpose, matricial product and matricial 
# sum operations, using a 100x100 matrix. Number of operations is equal to 100 mi,
# divided in 100 blocks of 100 operations.

import numpy as np
import time
import csv

#-----------------------DEFINES AND VARIABLES_INIT-----------------------------

block = 10000000
numBlocks = 100
transposeTimes = []
productTimes = []
sumTimes = []
totalTimetranspose = 0
totalTimeProduct = 0
totalTimeSum = 0

#create csv
w = csv.writer(open("times.csv", "w", newline=''))

#matrix 100x100 filled with random values(0-9)
m = np.random.randint(10, size=(100, 100))

#--------------FUNCTIONS-------------------------------------

#transpose matrix
def transposeMatrix(matrix):
    for j in range(numBlocks):
        initialTime = time.perf_counter()
        for i in range(block):
            c = np.transpose(matrix)
        transposeTimes.append(time.perf_counter() - initialTime)
        #print(transposeTimes[j])

#matricial product
def matricialProduct(matrix):
    for j in range(numBlocks):  
        initialTime = time.perf_counter()
        for i in range(block):
            c = matrix*matrix
        productTimes.append(time.perf_counter() - initialTime)
        #print(productTimes[j])

#matricial sum
def matricialSum(matrix):
    for j in range(numBlocks):
        initialTime = time.perf_counter() 
        for i in range(block):
            c = m+m
        sumTimes.append(time.perf_counter() - initialTime)
        #print(sumTimes[j])

#insert in csv
def insertCsv(array,totalTime):
    
    w.writerow(["Block process times"])

    for i in range(numBlocks):
        w.writerow([i+1, array[i]])
    
    w.writerow(["....."])
    w.writerow(["TOTAL",totalTime])

#----------------------------MAIN CODE--------------------------------------

##transpose operations
# transposeMatrix(m)
# for i in range(numBlocks):
#     totalTimetranspose = totalTimetranspose + transposeTimes[i]
# print(totalTimetranspose)
# insertCsv(transposeTimes, totalTimetranspose)

##product operations
# matricialProduct(m)
# for i in range(numBlocks):
#     totalTimeProduct = totalTimeProduct + productTimes[i]
# print(totalTimeProduct)
# insertCsv(productTimes, totalTimeProduct)

#sum operations
matricialSum(numBlocks)
for i in range(100):
    totalTimeSum = totalTimeSum + sumTimes[i]
print(totalTimeSum)
insertCsv(sumTimes, totalTimeSum)

