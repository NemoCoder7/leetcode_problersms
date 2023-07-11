class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        result = []
        capi = title.split()
        for i in capi:
            if len(i) < 3:
                result.append(i.lower())
            else:
                result.append(i.title())
        return " ".join(result)
