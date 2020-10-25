for i in range(1,999):
    vec = str(i)
    if int(i) > 99 and int(vec[0])+int(vec[1])+ int(vec[2])<9 :
        vec1= print(vec)
    elif 10<int(i)<99 and int(vec[0])+int(vec[1])<9:
            vec2 =print(vec)
    elif int(i)<10 and int(vec[0])<9:
                vec3 = print(vec)
print(vec1,vec2,vec3,sep=' ')
        
