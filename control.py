'''
control statement:
if cond:
    success statement
else:
    fail statement
'''

entry=int(input("Enter the amount to get entry: "))
if entry>=50:
    print("now u can enter game zone to watch")
    bucks=int(input("Tell us how muh amount u have: "))
    if bucks>=200:
        print("u can play twist monster")
    if bucks>=350 and bucks<500:
        print("u can play rapid river")
    if bucks>=500 and bucks<750:
        print("u can play 3D wonder land")
    else:
        print("simply watch")
else:
    print("u r not suppose to go inside")
