class Solution:
    def kWeakestRows(self, mat, k):
        dic = {i : sum(row) for i , row in enumerate(mat)}
        sorted_dic = dict(sorted(dic.items(), key=lambda x : x[1]))
        key_lst = list(sorted_dic.keys())
        return key_lst[:k]
