from random import randint

dice_roll_total_num = 0
total_outcome = []

def roll():
    dice_roll_1 = randint(1, 6)
    dice_roll_2 = randint(1, 6)
    dice_outcome = [dice_roll_1, dice_roll_2]
    dice_sum = dice_roll_1 + dice_roll_2

    global dice_roll_total_num, total_outcome
    dice_roll_total_num += 1
    total_outcome.extend(dice_outcome)

    print("The outcome of the first & second dice: " + str(dice_outcome))
    print("The sum of the dice: " + str(dice_sum))
    print("You've rolled " + str(dice_roll_total_num) + " times\n")

    print("\nThe total outcomes are:")
    print(total_outcome)


while (True):
    prompt = input("Would you like to roll the dice? (Y/N) \n").upper()
    if prompt == 'Y':
        roll()
    elif prompt == 'N':
        break
    else:
        print("Invalid input \n")
        continue


def statistics():
    # This will be used to see how closely the results match up with statistical expectations
    print("For 1: " + str(total_outcome.count(1) / len(total_outcome)))
    print("For 2: " + str(total_outcome.count(2) / len(total_outcome)))
    print("For 3: " + str(total_outcome.count(3) / len(total_outcome)))
    print("For 4: " + str(total_outcome.count(4) / len(total_outcome)))
    print("For 5: " + str(total_outcome.count(5) / len(total_outcome)))
    print("For 6: " + str(total_outcome.count(6) / len(total_outcome)))

    print("\nHow closely did this match up with the expected value of " + str(round((1/6), 3)) + " ?\n")

prompt_2 = 0
while (prompt_2 != 1):
    prompt_2 = input("Would you like to see how often each number showed up? (Y/N) \n").upper()
    if prompt_2 == 'Y':
        statistics()
        prompt_2 = 1
    elif prompt_2 == 'N':
        prompt_2 = 1
    # else:
    #     print("Invalid input \n")
    #     continue

