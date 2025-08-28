import random

print("Rock, Paper, Scissors")
print("Rules:\n Choose Rock, Paper or Scissors to Play. Quit to Stop Playing")
choice=["rock","paper", "scissors"]
user_score=0
computer_score=0
user1=input("Username: ")

while True:
    
    user=input("Choose Rock, Paper or Scissors: ").lower()
    if user=="quit": 
        print("Final Score:")
        print(f"{user1}: {user_score}| Computer: {computer_score}")
        break
    if user not in choice:
        print("Invalid Input Try Again.") 
        continue
    computer_choice=random.choice(choice)
    print(f"Computer {computer_choice}")
    if computer_choice==user:
        print("Its a Tie")
        user_score=0
        print(f"{user1}: {user_score}| Computer: {computer_score}")
        
    elif (user=="rock" and computer_choice=="scissors") or (user=="paper" and computer_choice=="rock") or (user=="scissors" and computer_choice=="paper"):
        print("You Win")
        user_score+=1
        print(f"{user1}: {user_score}| Computer: {computer_score}")
        
    else:
        print("You Lost")
        print(f"{user1}: {user_score}| Computer: {computer_score}")
        computer_score+=1
        
