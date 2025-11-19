# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: true
# Explanation: b[] is a subset of a[]
# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: false
# Explanation: b[] is not a subset of a[]
# Constraints:
# 1 <= a.size(), b.size() <= 105
# 1 <= a[i], b[j] <= 106

class Solution:
    # Two - pointer approach
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        i = 0
        j = 0
        m = len(a)
        n = len(b)
        
        while i < m and j < n:
            if a[i] < b[j]:
                i += 1
            elif a[i] == b[j]:
                i += 1
                j += 1
            else:
                return False       
        return j == n

    # Hashing approach with library    
    from collections import Counter    

    def isSubset(self, a, b):
        freq_map = self.Counter(a)
        
        for num in b:
            if freq_map[num] > 0:
                freq_map[num] -= 1
            else:
                return False
        return True
        
    # Hashing approach without library (Manual) 
    def isSubset(self, a, b):
        map = {}
        for num in a:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        
        for num in b:
            if num not in map or map[num] == 0:
                return False
            map[num] -= 1
        return True
    
if __name__ == "__main__":
    a = [11, 1, 13, 21, 3, 7]
    b = [11, 3, 7, 1]
    obj = Solution()
    print(obj.isSubset(a, b))