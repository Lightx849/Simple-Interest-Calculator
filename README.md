# Simple-Interest-Calculator

def interest():

    p = int(input("Enter p (principal): "))
    t = int(input("Enter t (time): "))
    r= float(input("Enter r (rate): "))

    a = (p * t * r) / 100

    return a 

total_interest = interest()

print(total_interest)
