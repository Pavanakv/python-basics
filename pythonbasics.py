from datetime import datetime
time=input("Enter the Time in Hours and minutes in AM/PM:")
times=datetime.strptime(time,"%I:%M %p")
if times.hour==8:
    print("Its Breakfast time!")
elif times.hour==13:
    print("Its Lunch time!")
elif times.hour==20:
    print("Its Dinner time!")
else:
    print("Its not meal time!")   
