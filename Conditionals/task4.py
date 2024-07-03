listWithAllAvailableGrades = ["A", "B", "C", "D", "F"]

print("Insert your grade: ", end="")
grade = input();
grade = grade.upper()

while(grade not in listWithAllAvailableGrades):
    print("Invalid grade!")
    print("Insert your grade: ", end="")
    grade = input();

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Passing")
    case "F":
        print("Failing")

