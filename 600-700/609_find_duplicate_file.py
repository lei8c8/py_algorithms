class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        lookup = {}
        for path in paths:
            path = path.split()
            for i in range(1, len(path)):
                temp = path[i].split('(')
                content, fileName = temp[-1][:-1], temp[0]
                if content not in lookup:
                    lookup[content] = [path[0] + '/' + fileName]
                else:
                    lookup[content].append(path[0] + '/' + fileName)
        return [lookup[key] for key in lookup if len(lookup[key]) > 1]