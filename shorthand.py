#Shorthand:

accBal=3500.8

#accBal=accBal+2000

accBal+=2000
print("After 2000 deposited balaance is:",accBal)

accBal-=4000
print("After 4000 debited balance is: ",accBal)

temp=(accBal*6.1)/100

accBal+=temp
print("Afetr intrest credited balance is: ",accBal)


vikas,vinay=12,8
print(vikas,vinay)

vikas*=vinay
vinay=int(vikas/vinay)
vikas/=vinay

print(int(vikas),vinay)
