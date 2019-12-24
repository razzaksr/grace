'''
Operators:
arithmetic: + - * / %
shorthand: += -= *= /= %=
relational: >= <= < > == !=
logicals: and or not
member: in, not in
identity: is, is not
'''

machineBalance=12000
users=int(input("Enter the required amount: "))
if users<=machineBalance:
    if users%2000==0:
        machineBalance-=users
        print("Amount ",users," debited successfully")
    else:
        print("Denomination not matched")
else:
    print("Insufficient amount")
