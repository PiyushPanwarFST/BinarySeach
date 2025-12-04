class Solution:
    def searchInsertK(self, arr, k):
        n = len(arr)
        low = 0 
        high = n-1
        ans = n
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == k:
                return mid
            
            elif arr[mid] > k:
                ans = mid
                high = mid - 1
                
            else: 
                low = mid + 1
        
        return ans
        