import random 

  
while True: 
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n") 
    
      
   
    choice = int(input("Your turn: ")) 
   
    while choice > 3 or choice < 1: 
        choice = int(input("enter valid input: ")) 
          
 
    if choice == 1: 
        choice_name = 'Rock'
    elif choice == 2: 
        choice_name = 'paper'
    else: 
        choice_name = 'scissor'
          
    
    print("Your choice is: " + choice_name) 
    print("\nNow its computer's turn-") 
  
  
    comp = random.randint(1, 3)  

    if comp == 1: 
        comp_choice_name = 'Rock'
    elif comp == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print("\n"+choice_name + " V/s " + comp_choice_name) 
  
    # condition for winning 
    if((choice == 1 and comp == 2) or
      (choice == 2 and comp ==1 )): 
        print("paper wins => ", end = "") 
        result = "paper"
          
    elif((choice == 1 and comp == 3) or
        (choice == 3 and comp == 1)): 
        print("Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins =>", end = "") 
        result = "scissor"
  
    if result == choice_name: 
        print("User wins") 
    else: 
        print("Computer wins") 
          
    print("\nDo you want to play again? (Y/N)") 
    ans = input() 
  
  
    if ans == 'n' or ans == 'N': 
        break

print("\nThanks for playing")
