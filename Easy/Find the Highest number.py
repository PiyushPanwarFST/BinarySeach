Given an integer array a[] of size n, find the highest element of the array. The array will either be strictly increasing or strictly increasing and then strictly decreasing.
Note: a[i] != a[i+1] 

Input: 11, 1 2 3 4 5 6 5 4 3 2 1
Output: 6
Explanation: Highest element of array a[] is 6.

Input: 5, 1 2 3 4 5
Output: 5
Explanation: Highest element of array a[] is 5.
Your Task:
You don't need to read or print anything. Your task is to complete the function findPeakElement() which takes the array a[] as the input parameter and returns the highest element of the 
array.

Expected Time Complexity: O(log(n))
Expected Space Complexity: O(1)

Constraints:
2 <= n <= 106
1 <= a[i] <= 106

from typing import List

class Solution:
	def findPeakElement(self, arr):
	    n = len(arr)
		low = 0
		high = n - 1
		
		while low <= high:
		    mid = (low + high) // 2
		    
		    if mid == 0:
		        if arr[mid] > arr[mid+1]:
		            return arr[mid]
		        else: low = mid + 1
		    
		    elif mid == n-1 and arr[mid] > arr[mid-1]:
		        return arr[mid]

		    elif arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
		        return arr[mid]
		        
		    elif arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
		        low = mid + 1
		        
		    elif arr[mid - 1] > arr[mid] and arr[mid] > arr[mid + 1]: 
		        high = mid - 1
