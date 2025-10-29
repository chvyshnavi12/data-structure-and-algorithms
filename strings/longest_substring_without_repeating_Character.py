def longest_substring_without_repeating_char(strs):
    n=len(strs)
    seen=set()
    left=0
    maxs=0
    for right in range(n):
        while strs[right] in seen:
            seen.remove(strs[left])
            left+=1
        seen.add(strs[right])
        maxs=max(maxs,right-left+1)
    return maxs
print(longest_substring_without_repeating_char("abcabcbb"))