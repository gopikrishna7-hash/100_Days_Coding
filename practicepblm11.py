# HackerRank First and Last Index
# Given an unsorted array arr[] of integers and a key which is present in this array. 
# Find the start index (index where the element is first found from left in the array) 
# and end index (index where the element is first found from right in the array). Return an array of length 2 
# with elements start index and end index.

def findIndex (arr, key):
        #code here
        
        start=-1
        end=-1
        for i in range(len(arr)):
            if key==arr[i]:
                if start==-1:
                   start=i
                end=i
        
        return [start,end]
res=findIndex([1,2,3,5,3,54,3,2],3)
print(res)