from BubbleSortDone import kiwi_weight, kiwi_list
from time import time
 
kiwi_weight_og = kiwi_list['Weight(kg)'].copy()
 
#Sorted list is empty
def test_BubbleWorst():
 start= time()
 assert len(kiwi_weight) != 0
 print(time()-start)
 
 #First value is the lowest and last value is the highest
def test_BubbleBest():
 start= time()
 assert kiwi_weight[0] == 1.570
 assert kiwi_weight[699] == 4.143
 print(time()-start)
 
 #Number of elements are the same before and after sorting
def test_BubbleAvg():
 start= time()
 assert len([kiwi_weight]) == len([kiwi_weight_og])
 print(time()-start)
