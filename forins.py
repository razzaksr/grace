#for in loop using over structures

univ={"California":450,"Anna":200,"Haward":900,"Cambridge":1400,"IIT":700,"Anna":800}
gpay=("razzaksr@okaxis",8667002959,"sabari@okkvb",876567823,8667002959,"nathan@okandhra")
chairs=[250,780,120,400,800]


#print(univ,gpay,chairs)

for temp1 in univ.items():
    print(temp1)

for temp2 in gpay:
    print(temp2)

for temp3 in chairs:
    if temp3 >=500:
        print(temp3)
