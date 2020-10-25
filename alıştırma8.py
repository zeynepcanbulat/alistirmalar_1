sum = 0
toplam = 0
for i in range (100,1000):
    sum += 1
    vec = str(i)
    if vec[0]!=vec[1]!=vec[2]:
        toplam += 1 
fark = sum - toplam
print(fark)
