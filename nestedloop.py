# hiring process
'''
for hire in range(1,6):
    skill=input("Enter the skill set: ")
    if skill == "AI" or skill == "Data Science" or skill == "python":
        print("U r hired")
    else:
        print("Update yourself")
'''

for hr in range(1,5):
    print("Interview handling by hr person: ",hr)
    hire = 1
    while hire <=5:
        skill=input("Enter the skill set: ")
        if skill == "AI" or skill == "Data Science" or skill == "python":
            print("U r hired count of ", hire," by the HR",hr);hire+=1
        else:
            print("Update yourself")
