#Ticket Booking Simulation
booked_seats=0
total_seats=8
while booked_seats<=total_seats:
    seats=int(input("Enter the number of seats you wanted to book:"))
    if booked_seats==0:
        booked_seats+=seats
        print(f"successfully you have booked {seats} seats!!")
    else:
        print("sorry there is not enough seats available!!")
        break
print("Thnaks for using booking system")    
        
    
        
