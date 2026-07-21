class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        my_dict = {}
        low = 0
        for high in range(len(s)):
            if s[high] in my_dict:
                low = max(low,my_dict[s[high]] + 1)
            

            max_length = max(max_length, high - low +1)
            my_dict[s[high]] = high
            high += 1
        
        return max_length

            


        