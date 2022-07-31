def main():
    greeting = input("Greeting: ")
    
    if "hello" in greeting.lower():
        print("$0")
    
    elif greeting.lower()[0] == 'h':
        print("$20")
    
    else:
        print("$100")

if __name__ == "__main__":
    main()