def asalmi(i):
    if i<=2:
        return False
    for n in range(3,i,1):
        if i%n == 0:
            return False
        else:
            print("It is a prime number: ", i)
            return True
            
