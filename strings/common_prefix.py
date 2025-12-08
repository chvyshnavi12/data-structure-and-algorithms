def common_prefix(x):
    x.sort()
    cnt=0
    first,last=x[0],x[-1]
    for i in range(min(len(first),len(last))):
        if first[i]==last[i]:
            cnt+=1
    return first[:cnt]
str = ["flowers" , "flow" , "fly", "flight" ]
str1 = ["dog" , "dcat" , "danimal", "domonkey" ]
print(common_prefix(str1))