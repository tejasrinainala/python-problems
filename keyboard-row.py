class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            lower_word = word.lower()
            letters = set(lower_word)

            if letters.issubset(row1) or letters.issubset(row2) or letters.issubset(row3):
                result.append(word)

        return result

        
