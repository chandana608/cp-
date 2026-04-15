a=int(input())
def addition(a,b):
    sum=a+b
    palindrome(sum)
def palindrome(n):
    n=str(n)
    n1=n[::-1]
    if n==n1:
        print(n)
    else:
        n=int(n)
        n1=int(n1)
        addition(n,n1)

palindrome(a)
    