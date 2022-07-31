def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    
    if y == "+":
        print(f"{x+z:.1f}")
    elif y == "-":
        print(f"{x-z:.1f}")
    elif y == "*":
        print(f"{x*z:.1f}")
    elif y == "/":
        print(f"{x/z:.1f}")
    else:
        print("Not supported operands.")


if __name__ == "__main__":
    main()