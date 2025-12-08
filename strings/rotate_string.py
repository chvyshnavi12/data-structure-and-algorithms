def rotate_str(x,y):
    n=len(x)
    for i in range(0,n):
        newone=y[i:]+y[:i]
        if newone==x:
            return True
    return False
s = "abcde" 
goal = "cdeab"
print(rotate_str(s,goal))
s = "abcde" 
goal = "adeac"
print(rotate_str(s,goal))
def optimal(s,goal):
    return len(s)==len(goal) and goal in (s+s)
s = "abcde" 
goal = "adeac"
print(rotate_str(s,goal))
