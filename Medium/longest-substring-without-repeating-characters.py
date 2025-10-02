class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   # Stores last seen index of characters
        max_len = 0
        start = 0         # Left boundary of current window

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                # Move start to one after last occurrence of current char
                start = char_index[char] + 1
            char_index[char] = end
            max_len = max(max_len, end - start + 1)

        return max_len
