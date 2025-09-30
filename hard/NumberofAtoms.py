class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplier
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][element] += count

        result_counter = stack.pop()
        sorted_elements = sorted(result_counter.keys())

        result = ""
        for elem in sorted_elements:
            result += elem
            if result_counter[elem] > 1:
                result += str(result_counter[elem])

        return result
