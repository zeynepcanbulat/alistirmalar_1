sum= 0 
for i in range(1000,10000):
    vec = str(i)
    if vec[0]>vec[3]:
        sum+=1
print(sum)
