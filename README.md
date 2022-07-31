# kiwi_sort
Methods of sorting the weight of kiwis from a CSV file

# Code requirements
#1 - Visual Studio 2022

#2 - Python 3.10

#3 - Install pandas library (pip install pandas)

#4 - data.csv in the same folder as the code

# Sorting Techniques
The sorting techniques chosen for this project are as follow:

#1 - Bubble Sort Algorithm

A sorting technique that repeateadly swaps elements around until the lowest is at the start and the highest at the end of the list

#2 - Selection Sort Algorithm

The selection sort repeateadly finds elements from an unsorted list and sorts them into a sorted list in an ascending order until there's no elements left

#3 - Bucket Sort Algorithm

Elements are assigned to individual buckets where they are sorted using a comparative method - the insertion algorithm - and then organized into a sorted list

# Written codes and outputs

Bubble Sort
![BubbleSort](https://user-images.githubusercontent.com/110004264/181662248-5d7b331f-2de4-4a61-93c6-513eedad8625.png)
![BubbleSortResult](https://user-images.githubusercontent.com/110004264/181662262-5ac671d0-e70d-49ef-ac96-aa1d4f9911dc.png)

Selection Sort
![SelectionSort](https://user-images.githubusercontent.com/110004264/181662287-dc638853-3765-4090-b735-49d1119fa922.png)
![SelectionSortResult](https://user-images.githubusercontent.com/110004264/181662293-1dee4252-2cef-423e-b1bb-b896c071f96f.png)

Bucket Sort
![BucketSort](https://user-images.githubusercontent.com/110004264/181662306-c20d26b3-26de-4668-8222-05e422952f80.png)
![BucketSortResult](https://user-images.githubusercontent.com/110004264/181662323-ac2a408a-5827-41a5-b7ba-ca17af45e52b.png)


# Unit testing (Automated approach)

#1 Bubble Sort
![Test](https://user-images.githubusercontent.com/110004264/182005106-d5d01c86-1b8d-498b-be44-bbf8ca60b99d.png)
![TestResult](https://user-images.githubusercontent.com/110004264/182005107-c35a331c-f55a-4072-b61e-79b749b6ea79.png)


#2 Selection Sort
![Test](https://user-images.githubusercontent.com/110004264/182005113-58856f22-218a-4ff2-9636-ea79fe0887ca.png)
![TestResult](https://user-images.githubusercontent.com/110004264/182005117-e4c490a2-793b-4158-8986-42d30cc00bdc.png)


#3 Bucket Sort

![Test](https://user-images.githubusercontent.com/110004264/182005123-1285b231-f722-4271-9d60-cd67f3283871.png)
![TestResult](https://user-images.githubusercontent.com/110004264/182005124-191e91f2-4217-48b9-a618-369c96d10814.png)


# Most optimized sorting technique

Based on the elapsed time for the execution of each code (excluding debugging), we can determine that the Bucket Sort is the least time complex algorithm and therefore executes the fastest out of all the options.

Here's how they ranked:

#1 - Bucket sort: 0.020s

#2 - Selection sort: 0.915s

#3 - Bubble sort: 2.205s

# Debugging

All codes executed without warnings or errors

# PyPlot of the kiwi weight dataset

Unsorted List

  ![UnsortedList](https://user-images.githubusercontent.com/110004264/181661994-559bf6ef-64a0-40f4-956a-58dde5ddebc6.png)
  
Sorted List  

![SortedList](https://user-images.githubusercontent.com/110004264/181662064-a2320159-ea15-4f1b-87aa-b43911521b1b.png)


  
