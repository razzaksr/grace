'''
Loop Statement:
repeat the statements or logic

initialization
condition
step up/ iteration

#init
while cond:
    #repeat logic
    iter

for temp in range(init,cond,iter):
    #repeat logic

for temp in STRVar:
    #repeat logic
'''

#themepark water games

person=1#init
while person<=10:
    wt=int(input("Tell us ur weight: "))
    if wt >= 45:
        print("We let you to play")
    else:
        print("We won't let u")
    person+=1
