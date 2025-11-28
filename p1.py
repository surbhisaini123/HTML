#A wire is the form of Arc at an angle of 60 degrees and the radius of the arc is 42. The wire is converted into a square. Find the area of the square.


radius_of_arc=42
angle=60 
pi=3.14

Area_of_circumference= 2*pi*radius_of_arc

length_of_wire=(angle/360)*Area_of_circumference

side_of_square=length_of_wire/4

Area_of_square=side_of_square*side_of_square
print("AREA==",Area_of_square)