son = 10000 #son değerini arttırdıkça n sonsuza gidecek.
e_sayısı=1
çarpım=1
for n in range(0,son):
    çarpım = çarpım * (n+1)
    e_sayısı = e_sayısı + (1/çarpım)
    

print(e_sayısı)
