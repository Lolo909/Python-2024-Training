import math;

#1
print("Insert length of the rectangle:", end="");
length_rectangle = int(input());

print("Insert width of the rectangle:", end="");
width_rectangle = int(input());

print("The rectangle area is ", length_rectangle * width_rectangle);

#2
print("Insert first side of the triangle:", end="");
firstSide = int(input());

print("Insert second side of the triangle:", end="");
secondSide = int(input());

hypotenuse = math.sqrt(firstSide**2 + secondSide**2);

print("The hypotenuse of the triangle is ",hypotenuse);


