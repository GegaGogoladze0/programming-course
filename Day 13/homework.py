# დავალება 1
num1 = float(input("Please enter an integer: ")) 
if num1 < 0: print(str(num1) + " is negative") 
if num1 == 0: print(str(num1) + " equals zero") 
if num1 > 0: print(str(num1)+ " is positive")
# დავალება 2
num1 = int(input("Please enter your age"))

if num1 >= 18:
    print("Your are an adult and can vote")

else:
    print("You are underage and cannot vote")

# დავალება 3
while True:
    for i in range(1,11):
        print(i) if i == 5:
        break
    break


# დავალება 6
num1 = float(input("Please enter your grade: "))

if num1 == 10.0:
    print(" Your child studies well!")

if num1 == 8.0 or 9.0:
    print("Your child studies well, although he could do better and get the highest grade")

if num1 == 5:
    print("Your child doesn't study at all and needs to study more")

if num1 < 5:
    print("Your son has been expelled")
    




