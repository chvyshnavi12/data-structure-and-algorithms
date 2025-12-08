def beautySum(s):
    n = len(s)
    ans = 0
    
    for i in range(n):
        freq = [0] * 26
        
        for j in range(i, n):
            freq[ord(s[j]) - ord('a')] += 1
            
            # compute max and min freq for this substring
            max_f = 0
            min_f = float('inf')
            
            for f in freq:
                if f > 0:
                    max_f = max(max_f, f)
                    min_f = min(min_f, f)
            
            ans += (max_f - min_f)
    
    return ans
