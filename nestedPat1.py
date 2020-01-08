'''
right upper floyd pattern:
     #
    ##
   ###
  ####
 #####
######
'''

for line in range(1,7):
    for space in range(6-1,line-1,-1):
        print(" ",end="")
    for data in range(1,line+1):
        print("#",end="")
    print()

'''
right lower floyd pattern:
######
 #####
  ####
   ###
    ##
     #
'''

for line in range(6,0,-1):
    for space in range(6-1,line-1,-1):
        print(" ",end="")
    for data in range(1,line+1):
        print("#",end="")
    print()

'''
left upper floyd pattern:
#
##
###
####
#####
######
'''

for line in range(1,7):
    for data in range(1,line+1):
        print("#",end="")
    print()

'''
left lower floyd pattern:
######
#####
####
###
##
#
'''

for line in range(6,0,-1):
    for data in range(1,line+1):
        print("#",end="")
    print()
