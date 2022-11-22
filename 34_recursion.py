#factorial num using iterative method
def factorial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

fnum=int(input("enter a num "))
#print(f"factorial of {fnum} is {factorial_iterative(fnum)} using iterative")

# factorial num using recursive method
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

#print(f"factorial of {fnum} is {factorial_recursive(fnum)} using recursive")


#fibonacci number
# 0,1,1,2,3,5,8,13,21...
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(f"fibonacci num of {fnum} is {fib(fnum)}")