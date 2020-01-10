'''
pascal:
     #
    # #
   # # #
  # # # #
 # # # # #
# # # # # #
'''
for line in range(1,7):
    for space in range(6-1,line-1,-1):
        print(" ",end="")
    for data in range(1,line+1):
        print("#",end=" ")
    print()
'''
pyramid:
   #
  ###
 #####
#######
'''
rows=int(input("Enter how many rows u need: "))
limit=1
for line in range(1,rows+1):
    for space in range(rows-1,line-1,-1):
        print(" ",end="")
    for data in range(1,limit+1):
        print("#",end="")
    limit+=2;print()


'''
pyramid:
#######
 #####
  ###
   #
'''
limit=7
for line in range(4,0,-1):
    for space in range(4-1,line-1,-1):
        print(" ",end="")
    for data in range(1,limit+1):
        print("#",end="")
    limit-=2;print()
