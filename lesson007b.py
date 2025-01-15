# Write a program that returns the gravitational force between two bodies with
# masses M1 and M2 and a distance r, where G = 6.67e-11.
#  Gf = G * (M1*M2) / r^2

M1 = float(input("Please enter the mass for M1: "))
M2 = float(input("Please enter the mass for M2: "))
r = float(input("Please enter the distance: "))
G = 6.67e-11
Gf = G * (M1*M2) / r**2

print(f"The gravitational for for two masses: {M1} and {M2} at a distance {r} is {Gf}.")
