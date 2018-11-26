class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmail = set()
        for e in emails:
            localName, domainName = e.split('@')
            if '+' in localName:
                localName = localName[:(localName.index('+'))]
            email = ''.join(localName.split('.')) + '@' + domainName
            uniqueEmail.add(email)
        return len(uniqueEmail)
