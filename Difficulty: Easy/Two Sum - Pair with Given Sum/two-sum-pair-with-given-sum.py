class Solution:
	def twoSum(self, arr, target):
	    s = set()
	    for x in arr:
	       diff = target - x
	       
    	   if diff in s:
    	       return True
    	       
    	   s.add(x)
        
        return False
	   # arr.sort()
	   # n = len(arr)
	   # left = 0
	   # right = n - 1
	    
	   # while left < right:
	   #     sum = arr[left] + arr[right]
	        
	   #     if sum == target:
	   #         return True
	        
	   #     elif sum < target:
	   #         left += 1
	            
	   #     else:
	   #         right -= 1
	    
	   # return False
	   
	   
        
        # s = set()

        # for num in arr:
          
        #     # Calculate the complement that added to
        #     # num, equals the target
        #     complement = target - num
    
        #     # Check if the complement exists in the set
        #     if complement in s:
        #         return True
    
        #     # Add the current element to the set
        #     s.add(num)
    
        # # If no pair is found
        # return False
