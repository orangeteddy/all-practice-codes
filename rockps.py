while True:
    user = input("Rock, paper, or scissors? ")

    import random
    comp = random.randrange(1, 4)

    if comp == 1:
        comp = "rock"
    elif comp == 2:
        comp = "paper"
    elif comp == 3:
        comp = "scissor"

    if user == "rock" or user == "Rock":
        if comp == "rock":
            print("You chose", user, ", and the computer chose ", comp, ". It's a tie")
        elif comp == "scissor":
            print("You chose", user, ", and the computer chose ", comp, ". You win.")
        elif comp == "paper":
            print("You chose", user, ", and the computer chose ", comp, ". You Lose.")
        else:
            print("Error")
        
    elif user == "paper" or user == "Paper":
        if comp == "paper":
            print("You chose", user, ", and the computer chose ", comp, ". It's a tie")
        elif comp == "rock":
            print("You chose", user, ", and the computer chose ", comp, ". You win.")
        elif comp == "scissor":
            print("You chose", user, ", and the computer chose ", comp, ". You Lose.")
        else:
            print("Error")
        
    elif user == "scissor" or user == "Scissor":
        if comp == "scissor":
            print("You chose", user, ", and the computer chose ", comp, ". It's a tie")
        elif comp == "paper":
            print("You chose", user, ", and the computer chose ", comp, ". You win.")
        elif comp == "rock":
            print("You chose", user, ", and the computer chose ", comp, ". You Lose.")
