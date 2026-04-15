def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
while True:
    a=int(input())
    # print(a)
    if a=="#":
        break
    res1=is_prime(a)
    # print(res1)
    a=str(a)
    b=a[::-1]
    b=int(b)
    # print(b)
    res2=is_prime(b)
    if res1==True and res2==True:
        print(f"{a} is emirp")
    elif res1==True:
        print(f"{a} is prime")
    else:
        print(f"{a} is not prime") 

