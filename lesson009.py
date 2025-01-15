# Write a program that returns the gravitational force between two bodies with
# masses M1 and M2 and a distance r, where G = 6.67e-11.
#  Gf = G * (M1*M2) / r^2

m1 = float(input("M1: "))
m2 = float(input("M2: "))
r = float(input("Radius: "))
G = 6.67*10**(-11)
Gf = G*(m1*m2/r**2)

print('The gravitational force is',Gf)