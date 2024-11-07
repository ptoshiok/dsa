class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wordFinal = ''
        for i in range(max(len(word1), len(word2))):
            if (i < len(word1)):
                wordFinal += word1[i]
            if (i < len(word2)):
                wordFinal += word2[i]
        return wordFinal
