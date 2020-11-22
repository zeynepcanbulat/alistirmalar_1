
b = input("Please enter a number between 100 and 1000: ")

while int(b)<100 or int(b)>1000:
    print("The number isn't in the specified range")
    b = input("Please enter a number between 100 and 1000! : ")
    


if b == b[::-1]:
    print("it is a palindromic number")

else:
    print("it is not a palindromic number")
     

        
