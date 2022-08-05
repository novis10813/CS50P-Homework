def main():
    sentence = input("Input: ")
    vowels = ["a", "e", "i", "o", "u"]
    for i in sentence:
        if i.lower() in vowels:
            sentence = sentence.replace(i, "")
    print(f"Output: {sentence}")

if __name__ == "__main__":
    main()