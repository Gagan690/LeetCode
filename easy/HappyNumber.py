class Solution:
    def isHappy(self, n):
        set_number = set()
        while n != 1 and n not in set_number:
            set_number.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1

        num = int(input("Enter the number : "))
        if isHappy(num):
            print("true")
        else:
            print("false")
