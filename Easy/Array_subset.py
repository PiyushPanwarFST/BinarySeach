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