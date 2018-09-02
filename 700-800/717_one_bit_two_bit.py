class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0 
        last_step = 0
        while i < len(bits):
            if bits[i] == 0:
                i += 1
                last_step = 1
            else:
                i += 2
                last_step = 2
        return last_step == 2