keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
s=input()
newstring=""

for item in s:
    item=item.upper()
    if item==" ":
        pass
        newstring+=" "
    else:
        pos=keyboard.index(item)
        newstring+=keyboard[pos-2]
    
print(newstring.lower())
        