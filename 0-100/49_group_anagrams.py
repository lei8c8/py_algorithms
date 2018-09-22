class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d, res = {}, []
        for ele in strs:
            sorted_ele = ''.join(sorted(ele))
            if sorted_ele not in d:
                d[sorted_ele] = [ele]
            else:
                d[sorted_ele].append(ele)
        for k in d:
            res.append(d[k])
        return res
