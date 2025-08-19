class Solution:
    def letterCombinations(self, digits):
        data = {
            2 : ['a','b','c'],
            3 : ['d','e','f'],
            4 : ['g','h','i'],
            5 : ['j','k','l'],
            6 : ['m','n','o'],
            7 : ['p','q','r','s'],
            8 : ['t','u','v'],
            9 : ['w','x','y','z']
        }
        if len(digits) == 0:
            return []
        result = []
        digit_list = list(map(int,digits))

        # Initialize result with the first digit's combinations
        result = data[digit_list[0]]

        # Iterate through the remaining digits and their combinations
        for i in range(1, len(digit_list)):
            new_result = []
            for combination in result:
                for char in data[digit_list[i]]:
                    new_result.append(combination + char)
            result = new_result

        return result

print(Solution().letterCombinations("78"))
