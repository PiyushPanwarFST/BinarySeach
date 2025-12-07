#User function Template for python3


class Solution:
    def find(self, arr, x):
        n = len(arr)
        low = 0
        high = n - 1
        first_occ = -1
        last_occ = -1
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if arr[mid] == x:
                first_occ = mid
                high = mid - 1
                    
            elif  x < arr[mid]:
                high = mid - 1
                    
            elif arr[mid] < x:
                low = mid + 1
            
        # if first_occ == -1:
        #     return [-1, -1]
                    
        low = 0
        high = n - 1
        
        while low <= high:
            
            mid = low + (high - low)//2
            
            if arr[mid] == x:
                last_occ = mid
                low = mid + 1

            elif  x < arr[mid]:
                high = mid - 1
                    
            elif arr[mid] < x:
                low = mid + 1
                    
        
        return [first_occ, last_occ]
                