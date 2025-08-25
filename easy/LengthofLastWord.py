class Solution:
  def lenghtoftheLastWord(self, s):
    s = s.strip()
    words = s.split(" ")
    return len(words[-1])

print(Solution().lenghtoftheLastWord("luffy is the joyboy"))
