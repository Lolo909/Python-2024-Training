print("Lenght: ", end="")
lenght = int(input());

print("Width: ", end="")
width = int(input());

def calculateRectangleArea(lenght, width):
    return lenght * width

print("Rectangle area with lenght %d and width %d is %d" % (lenght, width, calculateRectangleArea(lenght, width)));
