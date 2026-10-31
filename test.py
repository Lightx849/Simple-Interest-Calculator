# Simple Interest Calculator

def sim_interest():

    principal = 0
    time  = 0
    rate = 0

    while True:
        print("Principal cannot be equal to zero")
        principal = int(input("Enter the principal(P):"))
        if principal <=0 :
            print("Number cannot be equal to zero")
        else:
            break

    while True:
        print("Time cannot be equal to zero")
        time = int(input("Enter the time(t):"))
        if time <= 0:
            print("number cannot be equal to zero")

        else:
            break

    while True:
        print("Rate cannot be equal to zero")
        rate = float(input("Enter the rate (R):"))
        if rate <= 0:
            print("number cannot be equal to zero")

        else:
            break

    
    Interest = (principal * time * rate) / 100

    return Interest

total_interest = sim_interest()
print(f"The total interest to be payed is : {total_interest}")
                  


