import random
gesture = ['s','g','w']

game = True
point = 0
cpoint=0
life = 5
while game:
    while life>0:
            computer_choice = random.choice(gesture)
            your_choice = input("chose s for snake or g for gun or w for water\n").lower()
            print("computer choice is", computer_choice)
            print('************************************')
            if computer_choice == your_choice:
                print("It's a Tie")
                print('your point is',point)
                life=life
                print('your remaining life is', life)
            elif computer_choice=='s' and your_choice == 'g':
                print('You won!')
                point+=1
                print('your point is',point)
                life-=1
                print('your remaining life is', life)
            elif computer_choice=='g' and your_choice=='s':
                print('you lose')
                cpoint+=1
                print('your point is',point)
                life-=1
                print('your remaining life is', life)
            elif computer_choice=='s' and your_choice == 'w':
                print('you lose')
                cpoint+=1
                print('your point is',point)
                life-=1
                print('your remaining life is', life)
            elif computer_choice=='w' and your_choice=='s':
                print('you won!')
                point+=1
                print('your point is',point)
                life-=1
                print('your remaining life is', life)
            elif computer_choice=='g' and your_choice=='w':
                print('you won!')
                point+=1
                print('your point is',point)
                life-=1
                print('your remaining life is', life)
            elif computer_choice=='w' and your_choice=='g':
                print('you lose')
                cpoint+=1
                print('your point is',point)
                life-=1
                print('your remaining life is',life)
            else:
                print("invalid input",your_choice)
                print('your point is',point)
                life-=1
                print('your remaining life is', life)
            print('************************************')
            print(f'your total point is {point}.')
            print('computer total point is',cpoint)
    if point > cpoint:
        print('finally you won the game!')
    elif point < cpoint:
        print('You lose finally')
    else:
        print('it is tie!!')
    print('************************************')

    resume=input('Do you wanna play again? type yes for yor no for n.\n').lower()
    if resume == 'y':
        game= True
    else:
        game = False
