Given an element x and a sorted array, arr[], find the indices of first and last occurrences of the x's in the array.
Note: If the number x is not found in the array, return an array containing -1 only.

Input: x = 3, arr[] = [1, 3, 3, 4]
Output: [1, 2]
Explanation: The first occurrence of X = 3 is at index = 1 and the last at index = 2.

Input: x = 5, arr[] = [1, 2, 3, 4]
Output: [-1]
Explanation: 5 is not present, so the answer is -1.

Expected Time Complexity: O(log n)
Expected Auxillary Space: O(1)

Constraints: 
1 <= arr.size() <= 105 
0 <= arr[i], x <= 109

class Solution: 
    def find_first(self, x, arr):
        n = len(arr)
        low = 0
        high = n - 1
        ind = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == x:
                ind = mid
                high = mid - 1
            elif x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        return ind
        
    def find_last(self, x, arr):
        n = len(arr)
        low = 0
        high = n - 1
        ind = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == x:
                ind = mid
                low = mid + 1
            elif x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        return ind
        
    def firstAndLast(self, x, arr):
        first_occ = self.find_first(x, arr)
        last_occ = self.find_last(x, arr)
        
        if first_occ == -1:
            return [-1]
        else:
            return [first_occ, last_occ]
