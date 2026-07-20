class Solution:
    def isPalindrome(self, s: str) -> bool:
        # step 1 clean the string
        cleaned = [c.lower() for c in s if c.isalnum()]

        #step 2 two pointers
        R = len(cleaned) - 1
        L = 0

        while L < R:

            if cleaned[L] != cleaned[R]:
                return False
            
            L += 1
            R -= 1
        return True

        