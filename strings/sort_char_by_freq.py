from collections import Counter
def sort_char_by_freq(s):
    count=Counter(s)
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [char for char, freq in sorted_items]
s = "tree"
print(sort_char_by_freq(s))