def mult_table(r, c):
    max_char = len(str(r*c)) + 1
    for i in range(r):
        row = ""
        for j in range(c):
            entry = str((j+1)*(i+1))
            num_spaces = max_char - len(entry)
            spaces = num_spaces * " "
            row += (spaces + entry)
        print(row)

print("This function will print an aligned ")
print("multiplication table with the number ")
print("of rows and columns you specify.")
m = int(input("How many rows?: "))
n = int(input("How many columns?: "))
mult_table(m,n)
