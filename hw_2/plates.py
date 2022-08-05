def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def rule_1(s:str):
    if s[:2].isalpha:
        return True
    return False


def rule_2(s:str):
    if (len(s) >= 2) and (len(s) <= 6):
        return True
    return False


def rule_3(s:str):
    is_num = 0
    is_letter = 0
    for i in s:
        if i.isalpha():
            is_letter += 1
            if is_num != 0:
                return False
        if i.isdigit():
            is_num +=1
    
    return True


def rule_4(s:str):
    for i in s:
        if i.isdigit():
            if int(i) == 0:
                return False
            return True


def rule_5(s:str):
    if s.isalnum():
        return True
    return False


def is_valid(s:str):
    '''
    1. Starts with 2 letters
    2. At least two letters, maximun six characters
    3. numbers should not in the middle of the plates
    4. first number should not be zero
    5. no marks allowed
    '''
    
    if rule_1(s):
        if rule_2(s):
            if rule_3(s):
                if rule_4(s):
                    if rule_5(s):
                        return True
    return False
        
            
if __name__ == "__main__":
    main()