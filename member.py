#Member operator: in, not in

stock=["Puma","Adidas","Reebok","Bata","VKC","Paragon"]

print("Checking Woodlands is available: ",("Woodlands" in stock))

print("Checking Bata is available: ",("Bata" in stock))

print("Checking Nike is not there: ",("Nike" not in stock))

print("Checking Puma is not there: ",("Puma" not in stock))


#identity
alpha,beta=90,12
print(alpha,beta)
print("are they sharing memory: ",(alpha is beta))
print("are they not sharing memory: ",(alpha is not beta))


beta=90
print(alpha,beta)
print("are they sharing memory: ",(alpha is beta))
print("are they not sharing memory: ",(alpha is not beta))
