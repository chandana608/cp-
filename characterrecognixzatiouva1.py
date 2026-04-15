while True:
    s=input()
    if s=="#":
        break
    if s=="1" or s=="4" or s=="78":
        print("+")
    elif s[-1]=="5" and s[-2]=="3":
        print("-")
    elif s[0]=="9" and s[-1]=="4":
        print("*")
    elif s[0]=="1" and s[1]=="9" and s[2]=="0":
        print("?")
    else:
        pass    