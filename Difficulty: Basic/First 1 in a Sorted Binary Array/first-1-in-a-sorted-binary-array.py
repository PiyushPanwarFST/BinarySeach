#User function Template for python3

class Solution:
    def firstIndex(self, arr):
        n = len(arr)
        low = 0
        high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == 1 and mid == 0:
                    return mid
            
            if arr[mid] == 0:
                low = mid + 1
                
            if arr[mid] == 1:
                
                # if arr[mid] == 1 and mid == 0:
                #     return mid
            
                # elif arr[mid] == 1 and mid == n-1:
                #     return mid
            
                if arr[mid - 1] == 1:
                    high = mid - 1
                else:
                    return mid
            
        return -1
            

