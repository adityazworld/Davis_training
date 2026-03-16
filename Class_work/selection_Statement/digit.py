#find our the gretest no. from the given digits

num = 3723
max_digit = 0

while num > 0:
     #get last digit
    digit = num % 10     
    if digit > max_digit:
        max_digit = digit
   #remove last digit
    num = num // 10       

print("Greatest digit is:", max_digit)