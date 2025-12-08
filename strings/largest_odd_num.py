def largest_odd(s):
    max_num=0
    curr=""
    for i in s:
        curr+=i
        if int(curr)%2==1:
            max_num=curr
    if max_num[0]=='0':
        return max_num[1:]
    return max_num
s ="0214638"
print(largest_odd(s))
def largest_odd(s):
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % 2 == 1:   # odd digit found
            return s[:i+1]       # return substring up to that digit
    return ""                    # no odd digit found

