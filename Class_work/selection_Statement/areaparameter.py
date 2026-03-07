#wap to find the area and perimeter of rectangle and validate the data wherever required
# taking input from the user

length = float(input("Enter the length of the rectangle: "))
# validating the length
if length < 0:
    exit("Error: Length cannot be negative.")

width = float(input("Enter the width of the rectangle: "))
# validating the width
if width < 0:
    exit("Error: Width cannot be negative.")

# calculating area and perimeter
area = length * width
perimeter = 2 * (length + width)

# displaying the results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)


'''Output:
Enter the length of the rectangle: 5
Enter the width of the rectangle: 3
The area of the rectangle is: 15.0
The perimeter of the rectangle is: 16.0
