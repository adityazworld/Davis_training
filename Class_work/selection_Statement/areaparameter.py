#wap to find the area and perimeter of rectangle and validate the data wherever required
# taking input  length from the user

length = float(input("Enter the length of the rectangle: "))
# validating the length
if length < 0:
    exit("Error: Length cannot be negative.")
# taking input breadth from the user

breadth = float(input("Enter the breadth of the rectangle: "))

# validating the breadth
if breadth < 0:
    exit("Error: Breadth cannot be negative.")

# calculating area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# displaying the results
print("--------------------------------")
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)


'''Output:
Enter the length of the rectangle: 5
Enter the breadth of the rectangle: 3
The area of the rectangle is: 15.0
The perimeter of the rectangle is: 16.0

