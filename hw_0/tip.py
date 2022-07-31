def main():
    meal = input("How much was the meal? ")
    percent = input("What percentage would you like to give?")
    
    meal = float(meal[1:])
    percent = float(percent[:-1])/100
    
    print(f"Leave ${meal*percent:.2f}")

if __name__ == "__main__":
    main()