sum = 0
for i in range(10000,100000):
    vec = str(i)
    if vec[0] == vec[3] and vec[1]==vec[4]:
        sum += 1 
print(sum)
