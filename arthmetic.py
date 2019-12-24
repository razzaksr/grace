# arithmetic:+ - * / %


markerCost=int(input("Enter cost of marker: "))
markerQty=int(input("Enter how many marker you have in stock: "))
print("marker qty: ",markerQty)
print("marker price: ",markerCost)
worth=markerCost*markerQty
print("total worth of marker: ",worth)



package=float(input("Total contract cost: "))
days=int(input("Number of working days: "))
perDay=package/days;
perDay=perDay*100
print("Per day earning is: ",perDay)


minBal=int(input("Enter the min balance u wish to open an account"))
print("Status is:",minBal%5000==0)
