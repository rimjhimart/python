#COMPOUND INTEREST CALCULATOR

principle=0
rate=0
time=0
while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle<=0:
        print("Principle can not less than or equal to 0")
while rate <=0:
    rate = float(input("Enter the Rate amount: "))
    if rate<=0:
        print("Rate can not less than or equal to 0")
while time <=0:
    time = int(input("Enter the time amount: "))
    if time<=0:
        print("Time can not less than or equal to 0")    
total = principle *pow(1+rate/100, time)           
print(f"Balance after {time} year/s: ${total:.2f}")