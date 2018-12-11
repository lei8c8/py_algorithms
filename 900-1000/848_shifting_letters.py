class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s = [ord(e) for e in list(S)]
        total, times = sum(shifts), []
        for i in range(len(shifts)):
            times.append(total)
            total -= shifts[i]
        s = [(s[i] + times[i] % 26) for i in range(len(shifts))]
        for i in range(len(s)):
            while s[i] > 122:
                s[i] -= 26
        return ''.join([chr(e) for e in s])