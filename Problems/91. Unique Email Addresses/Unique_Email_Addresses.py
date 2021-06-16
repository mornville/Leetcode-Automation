class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        i = 0
        uniqueEmails = []
        for email in emails:
            localName, domainName = email.split('@')
            # Removing content beyond +
            if '+' in localName:
                localName = localName[:localName.index('+')]
                            # Replacing every . with ""
            localName = localName.replace('.', '')
                        newEmail = localName +'@' + domainName
                        if newEmail not in uniqueEmails:
                uniqueEmails.append(newEmail)
            else:
                pass
                                return len(uniqueEmails)