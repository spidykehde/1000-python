while True:
    b=int(input("Enter num1:")) 
    c=int(input("Enter num2:"))
    a=input("select your operation +,-,*,%,/,**,// \n")

    match a:
        case "+":
            d = b+c;
            print("Sum of the numers:",d);
        case "-":
            d = b-c;
            print("Subtraction",d);
        case "*":
            d = b*c;
            print("Multiplication:",d);
        case "%":
            d = b%c;
            print("Modulo",d);
        case "/":
            d = b/c;
            print("Division",d);
        case "**":
            d = b**c;
            print("Answer of",b," power ",c," is ",d);
        case "-":
            d = b//c;
            print("Floor division :",d);
    again=input("want to calculate again? (y/n) :").lower()
    if again!="y":
        break;

