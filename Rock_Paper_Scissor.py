print("Hello! Lets play Rock , Paper , Scissor :)")
while True:
    you=input('''You need to choose Rock , Paper or Scissor
    Enter your choice:''').lower()
    comp="rock"
    print("You chose: ",you)
    print("Computer chose:",comp)
    if you==comp:
        print("It's a tie ;)")
    elif you=="scissor" and comp=="paper":
        print("You won (╥﹏╥)")
    elif you=="paper" and comp=="rock":
        print("You won (╥﹏╥)")
    elif you=="scissor" and comp=="paper":
        print("You won (╥﹏╥)")
    elif you in ["rock","paper","scissor"]:
        print("Computer won ( ˶ˆᗜˆ˵ )")
    else:
        print("Invalid choice! Try again")
    again=input('''DO YOU WISH TO PLAY AGAIN?
    type (yes or no?) : ''').lower()
    if again!="yes":
        print("Thanks for playing this game :)")
        break