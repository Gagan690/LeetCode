class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        all_words =  (s1 + " " + s2).split()
        word_count = Counter(all_words)
        result = [word for word, values in word_count.items() if values == 1]
        return result
