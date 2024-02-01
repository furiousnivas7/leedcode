class Solution(object):
    def lengthOfLongestSubstring(self, s):
        c = set()
        left = 0
        result = 0

        for i in range(len(s)):
            while s[i] in c:
                c.remove(s[left])
                left += 1
            c.add(s[i])
            result = max(result, i - left + 1)

        return result
