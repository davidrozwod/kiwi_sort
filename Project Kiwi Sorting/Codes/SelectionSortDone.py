#Import resource library
import pandas as pd
import time

#Setting start runtime for the code execution
st = time.time()
 
#Reading CSV list
kiwi_list = pd.read_csv('data.csv')

#Print original values before sorting                                         
print("\nBefore sorting:\n")

#Defining temporary values to variables  
def swap(kiwi_weight, b, a):
    temp = kiwi_weight[b]
    kiwi_weight[b] = kiwi_weight[a]
    kiwi_weight[a] = temp

#Start of Selection Sort function
def selection_sort(kiwi_weight):
   
    #Acquires the number of elements in the list
    size = len(kiwi_weight)
    
    #Loop start
    for b in range(size):
        min_index = b

        #Finding the smallest element and swapping it with the next value
        for a in range(b+1, size):
            if kiwi_weight[min_index] > kiwi_weight[a]:
                min_index = a
        if b != min_index:
            swap(kiwi_weight, b, min_index)

    return kiwi_weight
    #Loop end

if __name__ == '__main__':

    #Retriving Weigth column from the CSV file
    kiwi_weight = kiwi_list['Weight(kg)'].copy()

    #Print results
    print("Given values : {}".format(kiwi_weight))
    print("Values after selection sort : {}".format(selection_sort(kiwi_weight)))

#Setting end runtime for the code execution
et = time.time()
elapsed_time = et - st

#Print elapsed time for the code execution
print('Execution time:', elapsed_time, 'seconds');


         
