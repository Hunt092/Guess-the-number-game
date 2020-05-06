import tkinter as tk
#--------------The main window----------------#
root= tk.Tk()
root.title("GUESS THE NUMBER")
#----------------------------------------------#


#------------------Global variables------------#
height = 600
width = 800
maxChances =int( )
randomNum = int( )     #'Comic Sans MS'
#----------------------------------------------#
title_font=('Cooper Black',20,'bold')
declaration_font=('Cooper Black',15,'bold')
button_font=('Berlin Sans FB Demi',20,'bold')
text_font=('Comic Sans MS',15)
#------------------------THE back Working FUnctions----------------#
def difficulty(answer):
    """Once the difficulty is set according to it the number of chances are set
    and the value is return by to the Game function"""
    if answer =="Easy":
        
        mess=tk.Label(game,text="You have to guess a number between 0 to 50\n",bd=15,relief='raised',font=('Cooper Black',15))
        mess.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.2)
        
    elif answer == "Medium":
        mess=tk.Label(game,text="You have guess a number between 0 to 100\n",bd=15,relief='raised',font=('Cooper Black',15))
        mess.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.2)
       
    elif answer == "Hard":
        mess=tk.Label(game,text="You have to guess a number between 0 to 150\n",bd=15,relief='raised',font=('Cooper Black',15))
        mess.place(relx=0.05,rely=0.01,relwidth=0.9,relheight=0.2)
        
     
def RanNum(answer):
    """Once the difficulty is set according to it the range of number to be
    guessed is set  and a random number in it generated randomly and returned 
    to the game function"""
    import random # it is a module which is used to generate random numbet

    if answer =="Easy":
        return random.randint(0,50)
        
    elif answer == "Medium":
       return random.randint(0,100)
    elif answer == "Hard":
        return random.randint(0,150)
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
    elif abstract<=5:
        return "almost near\n"
    elif abstract<=10:
        return "getting hot\n"
    elif abstract<=15:
        return "getting warm\n"
    elif abstract<=20:
        return "getting cold\n"
    elif difference>0:
        return "too low\n"
    else:
        return "too High\n"

def Game(maxChances,randomNum):
    """This is where all the main operation takes place and result are given"""
    input_text=gNum.get()
    Guessed = int(input_text)
    #print(randomNum) #its for debugging purpose prints the random number made by system
    # for chances in range (maxChances):
    text.delete(0.0, 'end')
    guessNum = Guessed
    result= matchNumber(randomNum, guessNum)
    #print(randomNum)
    if result == "Matched\n":
        Victory_frame()
        
    else:
        print_text ="The number you have guessed is "+ result
        text.insert(9.0,print_text)
        gNum.delete(0, 'end')
#-------------------------------------------------------------------#


#-----------------------THE screen bulding -------------------------#        
def difficulty_screen():
    mainMenu.destroy
    
    Difficulty.place(relheight=1,relwidth=1)
    
        
def Victory_frame():
    game.destroy
    
    victory.place(relheight=1,relwidth=1)
   
    
def again_pressed():
    Difficulty.option_clear
    victory.destroy
    
    Difficulty.place(relheight=1,relwidth=1)

    
def game_frame(answer):
    global maxChances
    global randomNum
    Difficulty.destroy
    game.place(relheight=1,relwidth=1,)
    maxChances= difficulty(answer)
    randomNum= RanNum(answer)
    
    
#print(tk.font.families())
#------------------------ the base canvas------------------------#
canvas = tk.Canvas(root,height=height, width=width)
canvas.pack()
#--------------------------------------------------------------#

#------------------------Main Menu Screen------------------------#
mainMenu = tk.Frame(root,bg="#00bfff",bd=15,relief='sunken')
mainMenu.place(relheight=1,relwidth=1, )

Start = tk.Button(mainMenu, text = "Start",command=difficulty_screen,
                  relief='flat',font=button_font,fg='navy blue',bg='#00bfff'
                  ,activebackground='#0059b3')
Start.place(relx=0,rely=0.65, relwidth=0.40, relheight=0.2)

Quit = tk.Button(mainMenu , text ="Quit",command=root.destroy,
                 relief='flat',font=button_font,fg='red',bg='#00bfff'
                 ,activeforeground ='#b30000',activebackground='#0059b3')
Quit.place(relx=0.6,rely=0.65,relwidth=0.4,relheight=0.2)

label= tk.Label(mainMenu,text="Main \nMenu",font=title_font,bd =20,relief='raised',bg='blue',)
label.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.25)
#--------------------------------------------------------------#


#-------------------------Difficulty Window------------------------#
Difficulty=tk.Frame(root,bg="#e60000",bd=15,relief='sunken') 

Text= tk.Label(Difficulty,text=" Choose your \ndiffulty",font=title_font,
               relief='raised',bd=10,)
Text.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.3)
              
Easy= tk.Button(Difficulty,text="Easy",command =lambda:game_frame("Easy"),
                relief='groove',bd=1.5,font=button_font
                ,activebackground="#990000")
Easy.place(relx=0.1,rely=0.5,relwidth=0.2,relheight=0.15)

Medium = tk.Button(Difficulty,text='Medium',command = lambda: game_frame("Medium"),
                   relief='groove',bd=1.5,font=button_font
                   ,activebackground="#990000")
Medium.place(relx=0.7,rely=0.5,relwidth=0.2,relheight=0.15)

Hard =    tk.Button(Difficulty,text='Hard',command = lambda: game_frame("Hard")
                    ,relief='groove',bd=1.5,font=button_font
                    ,activebackground="#990000")
Hard.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.15)
#--------------------------------------------------------------#


#-----------------------Game frame-----------------------------#
game = tk.Frame(root,bg='pink',bd=15,relief='sunken')

gNum=tk.Entry(game,bd=10,relief='flat',font=text_font)
gNum.place(anchor='n',relx=0.5,rely=0.25,relheight=0.25)

Submit= tk.Button(game, text="Submit?",command=lambda: Game(maxChances,randomNum)
                  ,font=button_font,bg='pink',activebackground='#ff3355')
Submit.place(anchor='n',relx=0.5,rely=0.55,)

text = tk.Text(game,wrap = 'word',relief='sunken',bd=5,font=text_font)
text.place(relx=0,rely=0.7,relwidth=1,relheight=0.3)
#--------------------------------------------------------------#


#------------------------Victory Frame------------------------#


victory = tk.Frame(root,bd=15,bg='#00cc00',relief='sunken')
# load = Image.open("confetti.png")
# render = ImageTk.PhotoImage(load,size='1920x1080')
# img = tk.Label(victory, image=render,relief='sunken')
# img.place(relx=0,rely=0,relwidth=1,relheight=1)

won= tk.Label(victory,text="CONGRATULATIONS YOU GUESSED \nTHE RIGHT NUMBER!!",
              bd=10,font=declaration_font,relief='raised',bg='#00cc00',fg='white')
won.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.25)

# again= tk.Button(victory,text="again",command=lambda: again_pressed())
# again.pack()

Exit= tk.Button(victory,text="Quit",command=root.destroy,font=button_font,
                fg="red",activebackground='#ff1a1a')
Exit.place(relx=0.375,rely=0.5,relwidth=0.25,relheight=0.1)
#--------------------------------------------------------------#


root.mainloop()

'''$~Yash Chavan '''