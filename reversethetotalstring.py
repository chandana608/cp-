s=input()
text=s.split(" ")
# print(len(text))
newtext=" "
for i in range(len(text)):
    text[i]=text[i][::-1]
    
result=' '.join(text)
print(result)