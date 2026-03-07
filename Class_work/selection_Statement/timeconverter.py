# program to input time in seconds and convert it to hours, minutes and seconds
# taking input from the user
second=int(input("Enter time in seconds: "))
# intialize hour and minute as 0
hour=0
minute=0
#calculating number of hours in given seconds
if second>=3600:
    hour=second//3600
    second=second%3600  
# calculating number of minutes in given seconds
if second>=60:          
    minute=second//60
    second=second%60

# displaying the result
print("Time :",hour,"hour(s)",minute,"minute(s)",second,"second(s)")

'''Output:
Enter time in seconds: 3665
Time : 1 hour(s) 1 minute(s) 5 second(s)    
Enter time in seconds: 7322
Time : 2 hour(s) 2 minute(s) 2 second(s)'''