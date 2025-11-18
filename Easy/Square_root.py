Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.
Floor value of any number is the greatest Integer which is less than or equal to that number.

Input: n = 4
Output: 2
Explanation: Since, 4 is a perfect square, so its square root is 2.
Input: n = 11
Output: 3
Explanation: Since, 11 is not a perfect square, floor of square root of 11 is 3.
Input: n = 1
Output: 1
Explanation: 1 is a perfect sqaure, so its square root is 1.
Constraints:
1 ≤ n ≤ 3*104

class Solution:
    def floorSqrt(self, n): 
        low = 1
        high = n
        res = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid ** 2 <= n:
                res = mid
                low = mid + 1
                
            else:
                high = mid - 1
            
        return res