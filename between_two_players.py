import sys
userl = input( "What's your name? : ") 
user2= input( "And your name? : ") 

userl_answer=input( "%s, do yo want to choose rock, paper or scissors? : " % userl)    
user2_answer = input( "%s, do yo want to choose rock, paper or scissors? : " % user2) 

def compare( u1, u2): 
    if u1 == u2:
        return("its a tie!" )
    
    elif u1 == 'rock': 
        if u2=='scissors': 
            return( userl, "wins!") 
        else: return( user2, "wins!") 
        
        
    elif u1 =='scissors': 
        if u2 == 'paper':
            return( userl, "wins!") 
        else: 
            return( user2 , "wins!")
        
        
    elif u1== 'paper': 
        if u2 =='rock': 
            return( userl, "wins!")
        else: 
            return( user2, "wins!")
                   
                   
    else: 
        return( "Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit( )
print(compare( userl_answer, user2_answer)) 
