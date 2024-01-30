list1 = input("Enter first list of numbers separated by commas: ")
list2 = input("Enter second list of numbers separated by commas: ")

# Convert the input strings to lists of integers
list3 = [int(n) for n in list1.split(",") if n]
list4 = [int(n) for n in list2.split(",") if n]

y = ''  # Initialize y as an empty string
for i in range(len(list3) - 1, -1, -1):
    x = str(list3[i])
    y = y + x
z = int(y)

y = ''  # Reset y for the second number
for i in range(len(list4) - 1, -1, -1):
    x = str(list4[i])
    y = y + x
r = int(y)

B = z + r
print(B)
