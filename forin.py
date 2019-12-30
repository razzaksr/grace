#scenario: hr recruitement

hiring =1
while hiring<=20:
    skill=input("Tell us ur skill set: ")
    if skill == "python" or skill == "iot" or skill == "ai":
        print("U r hired ",hiring);
    else:
        print("U need to update the required skill");hiring-=1;
    hiring+=1
