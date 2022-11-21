# hidden number #
# take a number
# ask user to guess it by 5 chance
# tell how many chances he took to guess the crrcet numbers

hidden_num = 13
count = 0
while count <=5:

    if count == 5:
        print("You lose.better luck next time. game over!")
        break
    else:
        guess = int(input('''enter a hidden number, ######hint########, It's in the range of 1 to 20'''))
        if guess == hidden_num:
            print("Kudos!! You guessed correct answer!! You won!\n""with",4-count,"lives left")
            break
        elif guess < 5:
            print(f"You are far away to the number!\nAnd you have {4-count} lives left.")
        elif guess < 10:
            print(f"Common think bigger!\n You left with {4-count} lives.")
        elif guess <= 15:
            print("you are too close\n""you have",4-count,"lives left" )
        elif guess > 20:
            print(f"o ohhh I think you didn't see the hint.\nyou have {4-count} lives left.")
        elif guess > 15:
            print(f"you went too far!\n You have {4-count} lives left.")
    count += 1
    continue




# n = 13
# for i in range(1,6):
#     a = int(input("enter"))
#     if i<5 or a==13:
#         if a<n:
#             print("think higher one")
#             print("you have left",5-i,"life")
#         elif a>n:
#             print("think lesser one")
#             print("you have left",5-i,"life")
#         else:
#             print("you won")
#             print("you took",i,"life to win")
#             break
#     else:
#         print("you guessed wrong numbers")
#         print("you have",5-i,"life left")
#         print("Game over")