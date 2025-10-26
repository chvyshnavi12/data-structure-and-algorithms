def group_anagram(values):
    result={}
    for i in values:
        newone="".join(sorted(i))
        if newone not in result:
            result[newone]=[]
        result[newone].append(i)
    print(list(result.values()))
values=["eat","tea","tan","ate","nat","bat"]
group_anagram(values)