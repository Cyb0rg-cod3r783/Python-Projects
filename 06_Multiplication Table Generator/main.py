number = int(input("Enter the number who's multiplication table you want to generate : "))
end = int(input("Enter till where you want to print the table of that number : "))

for i in range(1, (end+1)):
    print(f"{number} x {i} = {number*i}")