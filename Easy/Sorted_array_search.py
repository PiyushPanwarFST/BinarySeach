# Question:
# Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

# Input: arr[] = [1, 2, 3, 4, 6], k = 6
# Output: true
# Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
# Input: arr[] = [1, 2, 4, 5, 6], k = 3
# Output: false
# Exlpanation: Since, 3 is not present in the array, output is false.
# Input: arr[] = [2, 3, 5, 6], k = 1
# Output: false
# Constraints:
# 1 ≤ arr.size() ≤ 106
# 1 ≤ k ≤ 106
# 1 ≤ arr[i] ≤ 106

from typing import List
class Solution:
    # Linear Search Approach
    def findPair(self, arr: List[int], x: int) -> int:
        n = len(arr)
        arr.sort()
        
        for i in range(n):
            target = arr[i] + x
            if self.binary_search(arr, i+1, n-1, target):
                return True
        return False

    # Binary Search Code but getting TLE 
    def binary_search(self, arr, low, high, key):
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == key:
                return True
                
            elif arr[mid] < key:
                low = mid + 1
                
            elif arr[mid] > key:
                high = mid - 1

        return False
     
    # Two - Pointer apporach :
    def findPair(self, arr: List[int], x: int) -> int:
        i = 0
        j = i + 1
        n = len(arr)
        arr.sort()
        
        while j < n:
            diff = arr[j] - arr[i]
            
            if i == j:
                j += 1
                continue
            
            elif diff == x:
                return True
            
            elif diff < x:
                j += 1
            
            elif diff > x:
                i += 1
                
        return False

    # Hashing Approach 
    def findPair(self, arr: List[int], x: int) -> int:
        st = set()
        
        for num in arr:
            if ((num - x) in st) or ((num + x) in st) :
                return True
            
            st.add(num)

        return False       
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    k = 8
    obj = Solution()
    print(obj.searchInSorted(arr, k))