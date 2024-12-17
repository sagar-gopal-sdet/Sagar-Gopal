def find_first_occurrence(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                        if(needle == haystack[i:(i+len(needle))]):
                                return i

        return -1

print(find_first_occurrence("sadasticsad","sad"))