#Import resource library
import pandas as pd
import time

#Setting start runtime for the code execution
st = time.time()

#Reading CSV list
kiwi_list = pd.read_csv('data.csv')

#Print original list                                         
print("\nBefore sorting:\n")
print(kiwi_list)

#Start of Bubble Sort function
def bubbleSort(values):
    
  #Acquires the number of elements in the list
  for b in range(len(values)):    

   #Varriable to identify if the elements have been sorted
    sorted = False
   
    #Start of the comparison loop
    for a in range(0, len(values) - b - 1):

      #Checks if one value is greater than another
      if values[a] > values[a + 1]:

        #List values are set to a temporary variable and sorted
        temp = values[a]
        values[a] = values[a+1]
        values[a+1] = temp
        
        #Variable is set to true if the elements have been sorted
        sorted = True

    if not sorted:
      break
    #Loop end

#Retriving Weigth column from the CSV file
kiwi_weight = kiwi_list['Weight(kg)'].copy()

#Executing function
bubbleSort(kiwi_weight)

#Print results
print("\nArray after bubble sort:\n")
print(kiwi_weight)

#Setting end runtime for the code execution
et = time.time()
elapsed_time = et - st

#Print elapsed time for the code execution
print('Execution time:', elapsed_time, 'seconds')

         
