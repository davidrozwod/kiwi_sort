#Import resource library
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np

#Setting start runtime for the code execution
st = time.time()

#Reading CSV list 
kiwi_list = pd.read_csv('data.csv')

#Print original list                                         
print("\nBefore sorting:\n")
print(kiwi_list)

#Start of Bucket Sort function
def bucketSort(myList, noOfBuckets):
	#Determining maximium and minimium values in the list
	max_ele = max(myList)
	min_ele = min(myList)

	#Number of elements in the list
	rnge = (max_ele - min_ele) / noOfBuckets

	temp = []

	#Creating empty buckets to store the elements
	for i in range(noOfBuckets):
		temp.append([])

	#Inserting the values into the correct buckets
	for i in range(len(myList)):
		diff = (myList[i] - min_ele) / rnge - int((myList[i] - min_ele) / rnge)

		#Apends the elements to the lower list
		if(diff == 0 and myList[i] != min_ele):
			temp[int((myList[i] - min_ele) / rnge) - 1].append(myList[i])

		else:
			temp[int((myList[i] - min_ele) / rnge)].append(myList[i])

	#Sort each bucket individually
	for i in range(len(temp)):
		if len(temp[i]) != 0:
			temp[i].sort()

	#Insert sorted elements into original list
	k = 0
	for lst in temp:
		if lst:
			for i in lst:
				myList[k] = i
				k = k+1


#Number of buckets (one per element)
noOfBuckets = 700

#Retriving Weigth column from the CSV file
myList = kiwi_list['Weight(kg)'].copy()

#Execute Bucket Sort function
bucketSort(myList, noOfBuckets)

#Print results
print("\nArray after bucket sort:\n")
print(myList)

#Setting end runtime for the code execution
et = time.time()
elapsed_time = et - st

#Print elapsed time for the code execution
print('Execution time:', elapsed_time, 'seconds');

#Code for plotting graph
"""
#Setting the number of kiwis
kiwi_number = list(range(0, 700))

#Variables for axys x and y
x = np.array([myList])
y = np.array([kiwi_number])

#Plotting the graph
plt.axis([0, 700, 1.5, 4.2])
plt.ylabel('Kiwi Weight')
plt.xlabel('Kiwi')
plt.plot(y, x, linestyle='-', marker='o', color='b')
plt.show()
"""
         
