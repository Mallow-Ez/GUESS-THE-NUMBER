import emoji
import random
from tkinter import *

# ========================== GLOBAL VARIABLES ==========================

secret_number = 0
max_attempts = 0
attempts_left = 0

# ========================== LEVEL FUNCTION ==========================

def level(level):
    global secret_number, max_attempts, attempts_left

    if(level == "EASY"):
        max_attempts = 7
    elif(level == "MEDIUM"):
        max_attempts = 5
    elif(level == "HARD"):
        max_attempts = 3

    attempts_left = max_attempts
    secret_number = random.randint(1,100)
    
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    result_label.config(text="")
    entry.delete(0,END)

    entry.config(state=NORMAL)
    Guess_Button.config(state=NORMAL)
    end_frame.pack_forget()
    entry.delete(0,END)

    show_frame(game_frame)

# ========================== CHECK GUESS FUNCTION ==========================

def check():
    global attempts_left
    try:
        guess = int(entry.get())
    except:
        result_label.config(text="Enter a Valid Number..!")
        return
    
    attempts_left -= 1
    attempts_label.config(text=f"Attempts Left: {attempts_left}")
    if(guess == secret_number):
        result_label.config(text=emoji.emojize(":party_popper:Congartulation! You Won!"), foreground="#FFEA00")
        end_game()
    elif(attempts_left == 0):
        result_label.config(text=emoji.emojize(f":crying_face:GAME-OVER! Number was {secret_number}"))
        end_game()
    elif(guess > secret_number):
        result_label.config(text="TOO HIGH!")
    else:
        result_label.config(text="TOO LOW!")

# ========================== END GAME FUNCTION ==========================

def end_game():
    entry.config(state=DISABLED)
    Guess_Button.config(state=DISABLED)
    end_frame.pack(pady=20)

# ========================== MAIN WINDOW ==========================

window = Tk()
window.geometry("900x550")
window.title("GUESS THE NUMBER") 

icon = PhotoImage(file="GAME LOGO.png") 
window.iconphoto(True, icon)

window.config(background="#0F0F12") 

# ========================== FRAMES ==========================

menu_frame = Frame(window, background="#0F0F12")
rules_frame = Frame(window, background="#0F0F12") 
game_frame = Frame(window, background="#0F0F12")
for frame in (menu_frame, rules_frame, game_frame):
    frame.place(relwidth=1, relheight=1)

def show_frame(frame):
    frame.tkraise()

# ========================== MENU FRAME ==========================

Sub_Title_label = Label(menu_frame,
                text="Welcome To",
                  font=("Cologne", 20),
                    foreground="#02B5F5",
                      background="#0F0F12",
                        pady=15)
Sub_Title_label.pack()

Title_label= Label(menu_frame,
               text="GUESS THE NUMBER GAME",
                 font=("Cologne", 28, "bold"),
                   foreground="#DEAE02",
                     background="#0F0F12" )
Title_label.pack()

menu_button_frame = Frame(menu_frame, bg="#0F0F12")
menu_button_frame.pack(pady=150)

Play_Button = Button(menu_button_frame,
                      text="PLAY",
                        command=lambda: show_frame(rules_frame),
                          font=("Orbitron", 16, "bold"),
                            foreground="#E8E8E8",
                              activeforeground="#E8E8E8",
                                background="#0F0F12",
                                  activebackground="#0F0F12",
                                    width=14,
                                      height=2,
                                        borderwidth=5)
Play_Button.grid(row=0, column=0, padx=25)

Exit_Button = Button(menu_button_frame,
                      text="EXIT",
                        command=window.destroy,
                          font=("Orbitron", 16, "bold"),
                            foreground="#E8E8E8",
                              activeforeground="#E8E8E8",
                                background="#0F0F12",
                                  activebackground="#0F0F12",
                                    width=14,
                                      height=2,
                                        borderwidth=5)
Exit_Button.grid(row=0, column=1, padx=25)

# ========================== RULES FRAME ==========================--

Rules_Title_label = Label(rules_frame,
                text="RULES",
                  font=("Cologne", 30, "bold"),
                    foreground="#B7FF00",
                      background="#0F0F12")
Rules_Title_label.pack(pady=5)

rules = "1. The computer generates a random number between 1 and 100.\n" \
        "\n2. You must guess the correct number within limited attempts.\n" \
        "\n3. Choose a difficulty level before starting the game.\n" \
        "\n4. Each wrong guess will give you a hint (Too HIGH or Too LOW).\n" \
        "\n5.The game ends when you guess correctly or run out of attempts."

Rules_label = Label(rules_frame,
                text=rules,
                  font=("Times New Roman", 16),
                    foreground="#FFFFFF",
                      background="#0F0F12")
Rules_label.pack(pady=5)

All_The_Best_label = Label(rules_frame,
                text="All The Best",
                  font=("Bassy", 50, "bold"),
                    foreground="#008C6B",
                      background="#0F0F12")
All_The_Best_label.pack(pady=5)

rules_button_frame = Frame(rules_frame, bg="#0F0F12")
rules_button_frame.pack(pady=35)

Easy_Level = Button(rules_button_frame,
                     text="EASY",
                      font=("Orbitron", 16, "bold"),
                        foreground="#E8E8E8",
                          activeforeground="#E8E8E8",
                            background="#0F0F12",
                              activebackground="#0F0F12",
                                width=10,
                                  height=2,
                                    borderwidth=5)
Easy_Level.grid(row=0, column=0, padx=20)

Medium_Level = Button(rules_button_frame,
                     text="Medium",
                       font=("Orbitron", 16, "bold"),
                         foreground="#E8E8E8",
                           activeforeground="#E8E8E8",
                             background="#0F0F12",
                               activebackground="#0F0F12",
                                 width=10,
                                   height=2,
                                     borderwidth=5)
Medium_Level.grid(row=0, column=1, padx=20)

Hard_Level = Button(rules_button_frame,
                     text="Hard",
                       font=("Orbitron", 16, "bold"),
                         foreground="#E8E8E8",
                           activeforeground="#E8E8E8",
                             background="#0F0F12",
                               activebackground="#0F0F12",
                                 width=10,
                                   height=2,
                                     borderwidth=5)
Hard_Level.grid(row=0, column=2, padx=20)

Back_Button = Button(rules_button_frame,
                      text="BACK",
                        command=lambda: show_frame(menu_frame),
                          font=("Orbitron", 16, "bold"),
                            foreground="#E8E8E8",
                              activeforeground="#E8E8E8",
                                background="#0F0F12",
                                  activebackground="#0F0F12",
                                    width=10,
                                      height=2,
                                        borderwidth=5)
Back_Button.grid(row=2, column=0, columnspan=2, pady=20, padx=20)

Exit_Button = Button(rules_button_frame,
                      text="EXIT",
                        command=window.destroy,
                          font=("Orbitron", 16, "bold"),
                            foreground="#E8E8E8",
                              activeforeground="#E8E8E8",
                                background="#0F0F12",
                                  activebackground="#0F0F12",
                                    width=10,
                                      height=2,
                                        borderwidth=5)
Exit_Button.grid(row=2, column=1, columnspan=2, pady=20, padx=20)

Easy_Level.config(command=lambda: level("EASY"))
Medium_Level.config(command=lambda: level("MEDIUM"))
Hard_Level.config(command=lambda: level("HARD"))

# ========================== GAME FRAME ==========================--

Game_Title_label = Label(game_frame,
                          text="GUESS THE NUMBER GAME",
                            font=("Cologne", 35, "bold"),
                              foreground="#DEAE02",
                                background="#0F0F12")
Game_Title_label.pack(pady=10)

Instructions_label = Label(game_frame,
                            text="Enter A Number Between 1 & 100:",
                              font=("Times New Roman", 26),
                                foreground="#FFFFFF",
                                  background="#0F0F12")
Instructions_label.pack(pady=10)

entry = Entry(game_frame,
               font=("Arial", 17, "bold"),
                 justify="center",
                   width=5,
                     borderwidth=3)
entry.pack()

attempts_label = Label(game_frame,
                        text="Attempts Left: ",
                          font=("Times New Roman", 20),
                            foreground="#FFFFFF",
                              background="#0F0F12")
attempts_label.pack(pady=20)

result_label = Label(game_frame,
                      text="",
                        font=("Times New Roman", 20),
                            foreground="#FFFFFF",
                              background="#0F0F12")
result_label.pack(pady=20)

Guess_Button = Button(game_frame,
                        text="SUBMIT",
                          command=check,
                            font=("Orbitron", 16, "bold"),
                              foreground="#E8E8E8",
                                activeforeground="#E8E8E8",
                                  background="#0F0F12",
                                    activebackground="#0F0F12",
                                      width=10,
                                        height=2,
                                          borderwidth=5)
Guess_Button.pack(pady=10)

end_frame = Frame(game_frame, background="#0F0F12")

Restart_Button = Button(end_frame,
                          text="RESTART",
                            command=lambda: level("EASY" if max_attempts == 7 else
                                                  "MEDIUM" if max_attempts == 5 else
                                                  "HARD"),
                              font=("Orbitron", 16, "bold"),
                                foreground="#E8E8E8",
                                  activeforeground="#E8E8E8",
                                    background="#0F0F12",
                                      activebackground="#0F0F12",
                                        width=10,
                                          height=2,
                                            borderwidth=5)
Restart_Button.grid(row=0, column=0, padx=15)

Back_Button = Button(end_frame,
                      text="BACK",
                        command=lambda: show_frame(rules_frame),
                          font=("Orbitron", 16, "bold"),
                            foreground="#E8E8E8",
                              activeforeground="#E8E8E8",
                                background="#0F0F12",
                                  activebackground="#0F0F12",
                                    width=10,
                                      height=2,
                                        borderwidth=5)
Back_Button.grid(row=0, column=1, padx=15)

Exit_Button = Button(end_frame,
                      text="EXIT",
                        command=window.destroy,
                          font=("Orbitron", 16, "bold"),
                            foreground="#E8E8E8",
                              activeforeground="#E8E8E8",
                                background="#0F0F12",
                                  activebackground="#0F0F12",
                                    width=10,
                                      height=2,
                                        borderwidth=5)
Exit_Button.grid(row=0, column=3, padx=15)

show_frame(menu_frame)
window.mainloop()