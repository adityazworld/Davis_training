## program to display even factors of a number
num = int(input("Enter a number: "))
print("Even factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0 and i % 2 == 0:
        print(i)
'''Output:
Enter a number: 12
Even factors of 12 are:
2
4
6



