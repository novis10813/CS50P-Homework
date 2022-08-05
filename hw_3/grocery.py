d = {}

while True:
    try:
        item = input().upper()
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
            
    except EOFError:
        print()
        for key,value in sorted(d.items()):
            print(value, key)
        break