class Solution:
    def findNthDigit(self, n):
        # Determine the number of digits in the number containing the nth digit
        digits = 1
        count = 9
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10

        # Find the number that contains the nth digit
        # The first number with 'digits' number of digits is 10^(digits-1)
        first_num = 10**(digits - 1)
        num = first_num + (n - 1) // digits

        # Find the nth digit within the number
        digit_index = (n - 1) % digits
        return int(str(num)[digit_index])
