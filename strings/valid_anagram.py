def valid_angram(s,goal):
    return sorted(s)==sorted(goal)
s = "anagram" 
t = "nagaram"
print(valid_angram(s,t))