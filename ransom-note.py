# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        for i in ransomNote:
            if i in magazine:
                if ransomNote.count(i)<=magazine.count(i):
                    c+=1
        if c==len(ransomNote):
            return True
        else:
            return False
