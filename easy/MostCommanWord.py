import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        para = paragraph.lower()
        para = re.sub(r"[^a-z\s]"," ",para)
        para = para.split()
        para = Counter(para)
        hig_key = ['xyz',-1]
        for key , value in para.items():
            if key not in banned:
                if value > hig_key[1]:
                    hig_key[0] = str(key)
                    hig_key[1] = int(value)

        return hig_key[0]
