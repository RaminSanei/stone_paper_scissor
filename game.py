import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Rock Paper Scissors")
root.minsize(400, 500)
root.mainloop()

CHOICES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

# Main frames
header_frame = tk.Frame(root, bg="#4a7dff", height=80)
button_frame = tk.Frame(root, bg="#f0f0f0")
score_frame = tk.Frame(root, bg="#f0f0f0")
footer_frame = tk.Frame(root, bg="#607D8B")

# Grid layout
header_frame.pack(fill="x", pady=10)
button_frame.pack(fill="both", expand=True, padx=20, pady=10)
score_frame.pack(fill="both", expand=True, padx=20, pady=10)
footer_frame.pack(fill="x", pady=10)

# Status label
status_label = tk.Label(
    header_frame, 
    text="Make your choice!", 
    bg="#4a7dff", 
    fg="white",
    font=("Arial", 16)
)
status_label.pack(pady=20)

# Game buttons
rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 14))
paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 14))
scissors_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 14))

rock_btn.pack(side="left", expand=True)
paper_btn.pack(side="left", expand=True)
scissors_btn.pack(side="left", expand=True)

# Score labels
tk.Label(score_frame, text="Your Score", font=("Arial", 12)).grid(row=0, column=0)
tk.Label(score_frame, text="Computer Score", font=("Arial", 12)).grid(row=0, column=1)

player_score = tk.Label(score_frame, text="0", font=("Arial", 24))
computer_score = tk.Label(score_frame, text="0", font=("Arial", 24))

player_score.grid(row=1, column=0, pady=10)
computer_score.grid(row=1, column=1, pady=10)

reset_btn = tk.Button(
    footer_frame,
    text="Reset Game",
    command=lambda: [player_score.config(text="0"), computer_score.config(text="0")]
)
reset_btn.pack(pady=10)


def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 1 and computer == 3) or \
         (player == 2 and computer == 1) or \
         (player == 3 and computer == 2):
        return "player"
    else:
        return "computer"

def play(choice):
    computer_choice = randint(1, 3)
    result = determine_winner(choice, computer_choice)
    
    status_label.config(text=f"Computer chose: {CHOICES[computer_choice]}")
    
    if result == "player":
        player_score.config(text=str(int(player_score.cget("text")) + 1))
    elif result == "computer":
        computer_score.config(text=str(int(computer_score.cget("text")) + 1))

rock_btn.config(command=lambda: play(1))
paper_btn.config(command=lambda: play(2))
scissors_btn.config(command=lambda: play(3))


