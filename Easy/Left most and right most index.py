Given a sorted array with possibly duplicate elements. The task is to find indexes of first and last occurrences of an element X in the given
array.
Note: If the element is not present in the array return {-1,-1} as pair.

Input: N = 9, v[] = {1, 3, 5, 5, 5, 5, 67, 123, 125} , X = 5
Output: 2 5

Explanation: Index of first occurrence of 5 is 2 and index of last occurrence of 5 is 5.

Input: N = 9, v[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}, X = 7
Output: 6 6
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function indexes() which takes the array v[] and an integer X 
as inputs and returns  the first and last occurrence of the element X. If the element is not present in the array return {-1,-1} as pair.

Expected Time Complexity: O(Log(N))
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
1 ≤ v[i], X ≤ 1018

class Solution:
    def find_index(self, arr, x, findStart):
        n = len(arr)
        low = 0
        high = n - 1
        ind = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == x:
                ind = mid
                if findStart:
                    high = mid - 1
                else:
                    low = mid + 1
            
            elif x < arr[mid]:
                high = mid - 1
            else: 
                low = mid + 1
        return ind
        
    def indexes(self, v, x):
        first_index = self.find_index(v, x, True)
        last_index = self.find_index(v, x, False)
        
        return [first_index, last_index]
