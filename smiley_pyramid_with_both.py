limit = int(input("How many faces do you want? : "))
i = 0

while i < limit:
    for x in range(0, i+1):
        print("*", end="") 
    print("\n")
    i = i + 1