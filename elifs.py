# university seat allocation by cutoff using elif

cut=float(input("Tell us ur cutoff: "))
if cut>=119.25 and cut<150.5:
    print("Haward offers DataScientist")
elif cut>=145.1 and cut<260.8:
    print("Cambridge offers Cloud services")
elif cut>=180.9 and cut<450.7:
    print("DC offers Hetrogenious Computing")
elif cut>=500.8 and cut<1000.8:
    print("Haward offers Artifical Intelligence")
else:
    print("No university ready to offers you")
