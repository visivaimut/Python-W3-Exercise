limit = int(input("How many faces do you want? : "))
i = 0

while i < limit:
    j = i + 1
    k = 0
    while k < j:
        print("* ", end="")
        k = k + 1
    print("\n")
    i = j