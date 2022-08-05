def main():
    camel = input("camelCase: ")
    for i in camel:
        if i.isupper() and camel.index(i) != 0:
            index = camel.index(i)
            camel = camel[:index] + "_" + camel[index:]

    print(camel.lower())

if __name__ == "__main__":
    main()