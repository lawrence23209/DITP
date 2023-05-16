# import random and Tkinter packages

import random 
import tkinter

# initialise the window
# Create root widgets as main window
root = tkinter.Tk()

# Set geometry - the dimensions of the application window
root.geometry("400x400")

# Set title
root.title("Online Rock-Paper-Scissors Game")

# Define a dictionary that takes in the play options for the computer 
# Computer Value
computer_dict = (
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor",
)

# Create a function that resets the game
def reset_game():
    b1["state"] = 
    "active"
    b2["state"] = "active"
    b3["state"] = 
    "active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

# Create a function to disable the button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

    # Create three functions based on the three play options
    # to select the game winner

    # if player selects rock
    def player_rock():
    c_v = computer_dict[str(random.randint(0, 2))]
    if c_v == "Rock":
        match_result = "Tie!"
elif c_v == "Scissors":
match_result = "Player wins"
else:
match_result = "Computer wins"
else:

match_result = "Computer wins"
14.config(text=match_result)
11.config(text="Rock
    13.config(text=c_v)
    button_disable())

    # if player 
    selects paper 

    def player_paper():
        c_v= computer_dict(str(random.randint(0, 2)))
        if
    c_v == "Paper" :
            match result = "Tie!"
        elif c_v ==
    "scissors":
            match_result = "Computer Wins"
        else:
match_result = "Player Wins"
    14.config(text=match_result)

11.config(text="Paper
    13.config(text=c_v)
    button_disable())

    # If player
    selects scissors 

    def player_scissors():
        c_v = computer_dict[str(random.randint(0, 2))]

        if c_v == "Rock":
               match result = "Computer Wins"
               elif c_v ==
               "Scissors":
                       match_result = "Tie!"
                   else:
                       match_result =
            "Player Wins"
                14.config(text=match_result)
                11.config(text="Sissors")
                13.config(text=c_v)
                button_disable(
            
# Create Lables, Frames and Buttons for 
the GUI application
tkinter.label(root,
              text='Choose any one: Rock, Paper
Scissors,'
              font="Consolas"),
fg="blue").pack(pady=20)

frame = tkinter .Frame(root)

11 =
tkinter.label(frame,
                   text="player
font=10)

12 = tkinter.label(frame,
                   text="VS
                   
    font="Consolas")

13 = tkinter.label(frame, text="Computer",
font=10)

11.pack(side='left')

12.pack(side='left')
13.pack()

14 = tkinter.Label(root,
                   text="",
                           font="Consolas",
bg="white",
                           width=15,
                           borderwidth=2,
                            
                relief="Solid" )
        14.pack(pady=20)

frame1 =
tkinter.Frame(root)
frame1.pack()

b1 = tkinter.Button(frame1, text="Rock,
          font=8, width=7, bg="light blue,
command=player_rock")

b2 = tkinter.Button(frame1, text="Paper",
font=8, width=7, bg="light blue",
                    command=player_paper)

b3 = 
tkinter.Button(frame1, text="Scissors",
                    font=8, width=7,
bg="light blue",
                    command=player_scissors)

b1.pack(side='left',
padx=10)
b2.pack(side='left', padx=10)
b3.pack(padx=10)

tkinter.Button(root, text="reset game")
               
               font=10, fg="red",
grey", command=reset_game).pack(pady=20)

# Execute Tkinter
root.mainloop()





