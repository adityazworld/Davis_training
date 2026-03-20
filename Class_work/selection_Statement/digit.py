#find our the gretest no. from the given digits

num = int(input("Enter a number: "))
max_digit = 0

while num > 0:
     #get last digit
    digit = num % 10     
    if digit > max_digit:
        max_digit = digit
   #remove last digit
    num = num // 10       

print("Greatest digit is:", max_digit) 

'''Output:'''
##Enter a number: 5732    
##Greatest digit is: 7