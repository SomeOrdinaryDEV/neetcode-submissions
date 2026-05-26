class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned = cleaned.lower()
        n = len(cleaned)
        j = n-1

        for i in range(0, n):
            if cleaned[i] != cleaned[j]:
                return False
            j -= 1
        return True