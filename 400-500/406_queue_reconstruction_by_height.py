class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        people.sort(key=lambda x : (-x[0],x[1]))
        for p in people:
            answer.insert(p[1], p)
        return answer
