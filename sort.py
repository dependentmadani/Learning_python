# bubble sort algorithm
my_list = []
swapped = True
num = int(input("Number of element to sort: "))

for i in range(num):
    val = float(input("Enter your list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)
