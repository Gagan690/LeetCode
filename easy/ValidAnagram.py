class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        a=set(s)
        d1={}
        d2={}
        for i in a:
            d1[i]=s.count(i)
            d2[i]=t.count(i)
        if d1==d2:
            return True
        return False

