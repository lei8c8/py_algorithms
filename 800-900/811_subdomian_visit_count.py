class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        resList = []
        for domain in cpdomains:
            n = int(domain.split()[0])
            name = domain.split()[-1]
            nameList = name.split('.')
            for i in range(len(nameList)):
                if '.'.join(nameList[i:]) not in d:
                    d['.'.join(nameList[i:])] = n
                else:
                    d['.'.join(nameList[i:])] += n

        for k, v in d.items():
            resList.append(str(v) + ' ' + k)

        return resList


if __name__ == '__main__':
    solution = Solution()
    result = solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    print(result)