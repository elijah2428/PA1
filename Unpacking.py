# Ask for the number of elements
n = int(input("Enter number of elements: "))

# Create an empty list
list = []

# Get the list elements from the user
for i in range(n):
    elem = int(input(f"{i+1}: "))
    list.append(elem)

# Unpack the list into first, middle, and last
first, *middle, last = list

# Print the results
print(f"First: {first}, Middle: {middle}, Last: {last}")
