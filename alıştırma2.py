sum = 0
for i in range (1,1000000): #bitiş değerini arttırdıkça i sonsuza gidecek. 
    sum = sum + 1/(i**2)
    i += 1

from math import sqrt
pi_sayısı = sqrt(6*sum)
print(pi_sayısı)
