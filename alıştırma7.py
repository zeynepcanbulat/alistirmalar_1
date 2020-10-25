sum=0
for i in range(100,1000):
    vec = str(i)
    if int(vec[0]) + int(vec[1]) == int(vec[2]):
        sum +=1
        print(vec)
print("there is %d numbers" %(sum))        
