Question: Given an array, arr[] and an integer x, return true if there exists a pair of elements in the array whose absolute difference 
is x, otherwise, return false.

Input: arr[] = [5, 20, 3, 2, 5, 80], x = 78
Output: true

Explanation: Pair (2, 80) have an absolute difference of 78.
Input: arr[] = [90, 70, 20, 80, 50], x = 45
Output: false

Explanation: There is no pair with absolute difference of 45.
Input: arr[] = [1], x = 1
Output: false

Constraints:
1<= arr.size() <=106 
1<= arr[i] <=106 
0<= x <=10


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