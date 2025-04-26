class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        longest = s[0]

        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1] and len(temp) > len(longest):
                    longest = temp

        return longest
