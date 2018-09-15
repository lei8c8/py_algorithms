class Solution:
    def numRescueBoats(self, people, limit):
        left, right, res = 0, len(people) - 1, 0
        people.sort()
        while left < right:
            if people[right] + people[left] > limit:
                right -= 1
                res += 1
            elif people[right] + people[left] <= limit:
                right -= 1
                left += 1
                res += 1
        if left == right:
            res += 1
        return res