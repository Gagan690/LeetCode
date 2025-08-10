# from collection import Counter
import heapq
class Solution:
    def topKFrequent(self, words, k):
        
        """First Method Used"""
        # defdict = {}
        # for i in words:
        #     if i in defdict:
        #         defdict[i] += 1
        #     else:
        #         defdict[i] = 1
        # sorted_items = sorted(defdict.items(), key=lambda item: item[1], reverse=True)
        # result = [item[0] for item in sorted_items[:k]]

        # return result

        """Second Method Used"""
        

        count = Counter(words)

        heap = [(-freq,word) for word, freq in count.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)

        return result
