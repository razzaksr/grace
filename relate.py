# relational and logicals

#loan eligibility

ctc=float(input("Tell us ur annual ctc: "))
prop=int(input("Tell us the value if you have any property: "))
print("Status of CreditCard 50k=",ctc<2.5 and ctc>=1.8)
print("Status of PL of 1 lacks=",ctc>=2.5 and ctc<4.9)
print("Status of Business Loan=",ctc>=4.9 and prop>10)
print("Status of Home Loan of 5 lacks=",ctc>=8.5 or prop>15)
print("Status of IT filling: ",not ctc<2.5)
