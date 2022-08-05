def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            assert int(x) < int(y)
            ans = int(int(x)/int(y) * 100)
            if x == y:
                print("F")
            elif x == "0":
                print("E")
            else:
                print(f"{ans}%")
        except:
            pass
        else:
            break


if __name__ == "__main__":
    main()