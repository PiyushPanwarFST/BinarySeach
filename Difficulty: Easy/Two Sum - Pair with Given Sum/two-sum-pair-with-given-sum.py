class Solution:
	def twoSum(self, arr, target):
# 	  s = set()
# 	  for x in arr:
# 	    diff = target - x
	       
#     	   if diff in s:
#     	       return True
    	       
#     	   s.add(x)
#       return False
        s = set()
        for x in arr:
            diff = target - x
            
            if diff in s:
                return True
            
            s.add(x)
        return False
        

        # s = set()
        # for x in arr:
        #   diff = target - x
           
        #   if diff in s:
        #       return True
               
        #   s.add(x)
        
        # return False
	   