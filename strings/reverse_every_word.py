def reverse_word(x):
    q = x.split(" ")
    q.reverse()           # reverse in place
    return " ".join(q)

s = "welcome to the jungle"
print(reverse_word(s))
