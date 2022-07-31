from SelectionSortDone import selection_sort, kiwi_list
from time import time

kiwi_weight = kiwi_list['Weight(kg)'].copy()

averagecase= [kiwi_weight]

bestcase= sorted(averagecase)

worstcase= sorted(averagecase, reverse=True)

#Prompts error if list is execute but not sorted
def test_SelectionWorst():

 start= time()

 assert selection_sort(worstcase) == bestcase

 print(time()-start)

 #Ensures function executes and list is sorted
def test_SelectionBest():

 start= time()

 assert selection_sort(bestcase) == bestcase

 print(time()-start)

 #Ensures function executes
def test_SelectionAvg():

 start= time()

 assert selection_sort(averagecase) == bestcase

 print(time()-start)