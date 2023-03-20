sex = input("Enter your sex")
age = int(input("Enter your age here: "))

if sex == "man":
    if age < 18:
        print("You are not eligible to enter this bar.")
    elif age < 21 | age > 18:
        print("You may enter but you're underage to consume alcohol.")
    else:
        print("You can enter. Enjoy your night.")
elif sex == "woman":
    if age < 18:
        print("You are not eligible to enter this bar.")
    elif age < 21 | age > 18:
        print("say no to drinks")
    else:
        print("You can enter. Enjoy your night.")
else:
    if age < 18:
        print("You are not eligible to enter this bar.")
    elif age < 21 | age > 18:
        print("You may enter but you're underage to consume alcohol.")
    else:
        print("You can enter. Enjoy your night.")