import random
#randomizer in python

choice = int(input("1. Rock\n2. Paper\n3. Scissors\n\nPlease enter your choice correspondingly: "))
computer = random.randint(1,3)
hand = ["ROCK", "PAPER", "SCISSORS"]

if choice == computer:   
    print(f"\nYOU: {hand[choice-1]} \tDRAWS\t {hand[computer-1]} :COMPUTER\n")
    
if choice == 1 and computer == 2:
    print(f"\nYOU: {hand[choice-1]} \tVS\t {hand[computer-1]} :COMPUTER\n\nCOMPUTER WIN!!!\n")
elif choice == 1 and computer == 3:
    print(f"\nYOU: {hand[choice-1]} \tVS\t {hand[computer-1]} :COMPUTER\n\nYOU WIN!!!\n")

if choice == 2 and computer == 1:
    print(f"\nYOU: {hand[choice-1]} \tVS\t {hand[computer-1]} :COMPUTER\n\nYOU WIN!!!\n")
elif choice == 2 and computer == 3:
    print(f"\nYOU: {hand[choice-1]} \tVS\t {hand[computer-1]} :COMPUTER\n\nCOMPUTER WIN!!!\n")
    
if choice == 3 and computer == 1:
    print(f"\nYOU: {hand[choice-1]} \tVS\t {hand[computer-1]} :COMPUTER\n\nCOMPUTER WIN!!!\n")
elif choice == 3 and computer == 2:
    print(f"\nYOU: {hand[choice-1]} \tVS\t {hand[computer-1]} :COMPUTER\n\nYOU WIN!!!\n")

print("\n\n CONGRATULATIONS\n\n ")