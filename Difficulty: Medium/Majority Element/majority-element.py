class Solution:
    def majorityElement(self, arr):
        n = len(arr)/2
        map = {}
        
        for x in arr:
            map[x] = map.get(x, 0) + 1
        for key, val in map.items():
            if val > n:
                return key
        
        return -1
                        
            