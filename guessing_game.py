import random
num = random.randint(0, 100)
guess = 0
while guess != num:
    guess = int(input("Guess a number between 1 to 100: "))
    if guess == num:
        break
    elif abs(guess-num)<=5:
        if guess-num>0:
            print("Your answer is a little bit HIGH")
        else:
            print("Your answer is a little bit LOW")
    elif guess-num>10:
        print("Your answer is TOO HIGH")
    else:
        print("Your answer is TOO LOW")