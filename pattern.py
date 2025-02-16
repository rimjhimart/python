symbol = input("Enter the symbol you want to creat a pattern with: ")
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
for x in range(rows):
    for y in range(columns):
        print(symbol,end= "")
    print()


# output---->    Enter the symbol you want to creat a pattern with: *
# Enter the number of rows: 4 (user)
# Enter the number of columns: 5  (user)
# *****
# *****
# *****
# *****