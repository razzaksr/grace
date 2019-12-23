'''
Dictionary:{key:value}
insertion
read
update
delete
list
search
'''

univ={"California":450,"Anna":200,"Haward":900,"Cambridge":1400,"IIT":700,"Anna":800}

print(univ.get("Haward"))
print(univ)

univ["Holland"]=900
univ["IIT"]=1500

print(univ)

temp={}
temp=univ.copy()
print("temp copy: ",temp)
temp.pop("Haward")
temp.popitem()

print(univ,"\nTemp",temp)

print(univ.keys())
print(univ.values())
