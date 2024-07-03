print("Insert first number:", end="")
firstNumber = float(input())

print("Insert first number:", end="")
secondNumber = float(input())

print("Insert operation (+,-,*,/):", end = "")
operation = input();

match operation:
    case "+":
        print(firstNumber+secondNumber);
    case "-":
        print(firstNumber-secondNumber);
    case "*":
        print(firstNumber*secondNumber);
    case "/":
        print(firstNumber/secondNumber);