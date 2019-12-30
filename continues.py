#continue, break; scenario: open ticket distribution using for in range

for ticket in range(1,21):
    if ticket==4 or ticket==5 or ticket==9 or ticket==14 or ticket==18:
        print(ticket," Booked @ online");continue;
    else:
        amt=int(input("Enter the amount to travel in SL coach: "))
        if amt >= 290:
            print("U can travel in SL @",ticket)
        else:
            print("Please go to GNL")
    
