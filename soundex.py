while True:
    str1=""
    newstr=""
    a=input()
    # a=a.split()
    if a=="#":
        break
    a=a.upper()
    # print(a)
   
    soundex = {
    1: ["B","F","P","V"],
    2: ["C","G","J","K","Q","S","X","Z"],
    3: ["D","T"],
    4: ["L"],
    5: ["M","N"],
    6: ["R"]
    }
    for i in a:
        for key, value in soundex.items():
            if i in value:
               str1+=str(key)
            #    print(str1)
            #    print(key)
    
    for i in range(len(str1)):
        if i==0 or str1[i] != str1[i-1]:
            newstr += str1[i]
    print(newstr)
   