P = float(input("Enter Principal amount:"))
R = float(input("Enter Rate of interest:"))
T = float(input("Enter Time (in years):"))

SI = (P * R * T ) / 100
print("Simple Interest is:" , SI)

age = int(input("Enter your age:"))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are NOT eligible to vote")