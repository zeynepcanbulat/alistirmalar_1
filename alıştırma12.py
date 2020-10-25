for i in range (1000,2010):
    vec = str(i)
    if int(vec[0])+ int(vec[1])+ int(vec[2])+ int(vec[3]) == 2005-i:
        print(i)
