class Solution:
    # O(n) Time | O(1) Space, where n is length of string
    def canPermutePalindrome(self, s: str) -> bool:
        chars = {}
        for char in s:
            if char in chars:
                del chars[char]
            else:
                chars[char] = True
        
        if len(s) % 2 == 0:
            return len(chars) == 0
        else:
            return len(chars) == 1
        
