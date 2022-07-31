def main():
    ans = input("What is the answer to the great question of life? ")
    
    if ans.strip() == '42':
        print("yes")
    
    elif ans.lower().strip() == "forty-two":
        print("yes")
    
    elif ans.lower().strip() == "forty two":
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()