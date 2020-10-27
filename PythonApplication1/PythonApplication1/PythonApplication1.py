n1 = float(input("enter a positive number: "))
n2 = float(input("enter a positive number: "))
n3 = float(input("enter a positive number: "))
geom_mean = (n1 * n2 * n3) ** (1 / 3)            # finding a geometric mean of the entered numbers
fractional_part = geom_mean % 1                  # finding a fractional part of the geometric mean
print('fractional part:', fractional_part)

