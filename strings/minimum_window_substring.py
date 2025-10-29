from collections import Counter

class Solution:
    def minWindow(self, s, t):
        # Edge case
        if not s or not t or len(t) > len(s):
            return ""
        
        # Step 1: count required chars
        required = Counter(t)
        window = Counter()
        
        have, need = 0, len(required)
        res = ""
        min_len = float('inf')
        
        left = 0
        for right, char in enumerate(s):
            window[char] += 1
            
            # If this character satisfies one required char
            if char in required and window[char] == required[char]:
                have += 1
            
            # Step 2: when window is valid, try to shrink
            while have == need:
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    res = s[left:right+1]
                
                # remove leftmost char
                window[s[left]] -= 1
                if s[left] in required and window[s[left]] < required[s[left]]:
                    have -= 1
                left += 1  # move left boundary
        
        return res
