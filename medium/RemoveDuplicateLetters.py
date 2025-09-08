class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                continue

            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)

# Example Usage:
# print(Solution().removeDuplicateLetters("cbacdcbc"))
# print(Solution().removeDuplicateLetters("bcabc"))
