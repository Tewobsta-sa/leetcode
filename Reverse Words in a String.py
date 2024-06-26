class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = [word[::-1] for word in words]
        return ' '.join(result)
