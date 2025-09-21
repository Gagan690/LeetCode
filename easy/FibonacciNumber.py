class Solution:
    def fib(self, n: int) -> int:
        lst = [0,1]
        while len(lst) == n+1:
            lst.append(lst[-2] + lst[-1])
        return lst[-1]
