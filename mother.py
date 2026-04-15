while True:
    str1=input()
    if str1=="DONE":
        break
    str1=str1.replace(",","").replace(" ","").replace("!","").replace(".","")
    str1=str1.lower()
    # print(str1)
    result=str1[::-1]
    # print(result)
    if result==str1:
        print("You won’t be eaten!")
    else:
        print("Uh oh..")
    
        