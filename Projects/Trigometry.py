import math
# To Find Circumference
radius=float(input(f"What is the Radius of the Circle : "))
c = 2*math.pi*radius
print(f"The circumference of the circle is : {round(c,3)}")

# To Find The Area
Area =float(input(f"What is the Radius of Area : "))
Area = math.pi*math.pow(Area,2)
print(f"The Area Is : {round(Area,3)}")

#To find Hypotoneous
A = float(input(f" Side A = "))
B = float(input(f" Side B = "))
H = math.sqrt(pow(A ,2)+pow(B, 2))
print(f"The Hypoteneous of R.A.T : {round(H,3)}")