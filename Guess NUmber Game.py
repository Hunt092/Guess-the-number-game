
def Start():
    """The game starts with asking what difficulty you wanna start with and 
    then taking the key input to return the diffculty you have decided on,
    if the input given by user is none of the given 3 key None type is returned"""
    print("\n Are you ready to play the game? \n"
          "     choose the difficulty\n "
          "     Easy(1)       Medium(2)\n"
          "            Hard(3)\n"
          "          Enter(1/2/3)")
    key=input()
    if key=='1':
        return "Easy"
    elif key=='2':
        return "Medium"
    elif key=='3':
        return "Hard"
            
        
def difficulty(answer):
    """Once the difficulty is set according to it the number of chances are set
    and the value is return by to the Game function"""
    if answer =="Easy":
        
        print ("You have 5 chances to guess a number between 0 to 50\n")
        return 5
    elif answer == "Medium":
        print ("You have 3 chances to guess a number between 0 to 50\n")
        return 3
    elif answer == "Hard":
        print ("You have 5 chances to guess a number between 0 to 100\n")
        return 5
     
def RanNum(answer):
    """Once the difficulty is set according to it the range of number to be
    guessed is set  and a random number in it generated randomly and returned 
    to the game function"""
    import random # it is a module which is used to generate random numbet

    if answer =="Easy":
        return random.randint(0,50)
        
    elif answer == "Medium":
       return random.randint(0,50)
    elif answer == "Hard":
        return random.randint(0,100)
    """.randint() is the inbulit function in the random which generated a random 
    int with in the specified range"""
    
def matchNumber(random,guess):
    """ takes the guessed number and random numeber ie the input from user 
    and the genrated number from the system respectively,and the
    finds the differences and according sees if the guessed number is 
    same as random number and if not where does it stand in respective to it in
    value and respective is returned and used in Game function"""
    difference = random - guess
    abstract= abs(random-guess)
    
    if difference==0:
        return "Matched\n"
    elif abstract<3:
        return "almost near\n"
    elif difference>0:
        return "too low\n"
    else:
        return "too High\n"
    
def Game():
    """This is where all the main operation takes place and result are given"""
    answer = Start()
    maxChances= difficulty(answer)
    randomNum= RanNum(answer)
    
    chances = 0
    #print(randomNum) #its for debugging purpose prints the random number made by system
    if maxChances!= None:
        while chances<maxChances:
            chances+=1
            guessNum = int( input( "guessed numner\n"))
            result= matchNumber(randomNum, guessNum)
            #print(chances) print number of chances also for debugging
            if chances<maxChances:
                if result== "Matched\n":
                    break
                else:
                    print("Wrong!, your guess was " + result)  
                
        if result== "Matched\n":
            print("Congratulations its a  " + result)
            print("")
        
        else:
            print("You LOSE, the correct answer was " , randomNum)
                
                
    else:
        print("Invalid input")
        pass
            
if __name__=="__main__":
    game=input("Do you wanna play the game{y/n}\n")
    while game !='n':
        if game=='y':
            Game()
            game=input("Do you wanna play Again{y/n}\n")
        else:
            print("Invalid Input")
            game=input("Do you wanna play Again{y/n}\n")
    print('            Thank You for playing, Bub-BYEE')
    $~Yash
