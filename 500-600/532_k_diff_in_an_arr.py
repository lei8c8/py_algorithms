class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        if k== 0:
            mySet = set()
            prev = None
            nums.sort()
            for e in nums:
                if e != prev: 
                    prev = e
                    continue
                if e in mySet: continue
                mySet.add(e)          
            return len(mySet)
        lookup = set(nums)
        res = 0
        for e in lookup:
            if e + k in lookup:
                res += 1
        return res