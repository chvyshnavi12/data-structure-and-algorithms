def valid_palindrome(strs):
    n=len(strs)
    newone="".join(c.lower() for c in strs if c.isalnum())
    n=len(newone)
    j=n-1
    i=0
    while i<n:
        if newone[i]!=newone[j]:
            return False
        j-=1
        i+=1
    return True
print(valid_palindrome("A man, a plan, a canal: Panama"))