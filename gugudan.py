num = (input("Enter a number between 1 and 9: "))
print ("")

while type(num) == str:
    try:
        num = int(num)
        if num < 1 or num > 9: 
            print("Input error, try again.") 
            print(" ")
            num = input("Enter a number between 1 and 9: ")
            print("")
    except ValueError:
        print("Input error, try again.")
        print(" ")
        num = input("Enter a number between 1 and 9: ")
        print(" ")

for j in range (num):
    for i in range (1,10):
        print(num, "times", i, "is", num * i)
    num = num - 1
    print("")