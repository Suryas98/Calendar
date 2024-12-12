# Letter "P" pattern

def print_P():
    for row in range(6):
        if row == 0 or row == 3:
            print("**** ")
        elif row < 3:
            print("*  *")
        else:
            print("* ")

print("\nPattern for P:")
print_P()

# Letter "A" Pattern

def print_A():
    for row in range(5):
        if row == 0:
            print("  *  ")
        elif row == 1:
            print(" * * ")
        elif row == 2:
            print("*****")
        else:
            print("*   *")
print("\nPattern for A:")
print_A()
