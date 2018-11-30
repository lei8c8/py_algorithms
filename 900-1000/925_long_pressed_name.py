class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name[0] != typed[0] or name[-1] != typed[-1]: 
            return False
        p, last = 1, name[0]
        for i in range(1, len(name)):
            while typed[p] != name[i] and typed[p] == last:
                p += 1
                if p >= len(typed):
                    return False
            if typed[p] != name[i]:
                return False
            last = name[i]
            p += 1
        return True