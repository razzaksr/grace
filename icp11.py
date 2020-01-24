
#Answer for second question
userName = input("Enter USER NAME : ")
delCount = int(input("Enter the number of characters to be deleted : "))
startPoint = int(input("Start Point: "))
print("ORIGINAL USER NAME : " + userName)
userName=userName[:startPoint]+userName[(startPoint+delCount):]
print("USER NAME AFTER DELETING CHARACTERS : " + userName)
# to reverse the string
userName = userName[::-1]
print("USER NAME AFTER REVERSING : " + userName)


#Answer for third
para=input("Enter the paragraph: ")
print(para)
para=para.replace("python","pythons")
print(para)
