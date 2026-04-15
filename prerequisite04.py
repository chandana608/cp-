str1,str2=map(str,input().split())
i=0
for ch in str2:
    if i<len(str1) and ch==str1[i]:
        i+=1
if i==len(str1):
    print("YES")
else:
    print("NO")
