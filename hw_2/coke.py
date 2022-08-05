def main():
    due = 50
    print(f"Amount due: {due}")
    
    while True:
        try:
            coin = int(input("Insert Coin: "))
            assert coin in [25, 10, 5]
        except:
            pass
        else:
            due -= coin
            
            if due == 0:
                print(f"Change Owed: {due}")
                break
            
        print(f"Amount Due: {due}")


if __name__ == "__main__":
    main()