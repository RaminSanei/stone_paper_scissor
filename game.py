import tkinter as tk
from tkinter import messagebox
from random import randint
from PIL import Image, ImageTk
import requests
from io import BytesIO

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.minsize(450, 600)
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.choices = {
            1: "Rock",
            2: "Paper",
            3: "Scissors"
        }
        
        # Load images (placeholder URLs - replace with actual image URLs)
        self.images = {
            "Rock": self.load_image("https://cdn-icons-png.flaticon.com/512/3364/3364044.png"),
            "Paper": self.load_image("https://cdn-icons-png.flaticon.com/512/3364/3364056.png"),
            "Scissors": self.load_image("https://cdn-icons-png.flaticon.com/512/3364/3364064.png")
        }
        
        self.setup_ui()
    
    def load_image(self, url):
        try:
            response = requests.get(url, timeout=5)
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((80, 80), Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except:
            # Fallback if image loading fails
            return None
    
    def setup_ui(self):
        # Configure grid
        self.root.rowconfigure([0, 1, 2, 3], weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Status label
        self.lbl_status = tk.Label(
            master=self.root,
            text="Make your choice!",
            bg="#4a7dff",
            fg="white",
            height=2,
            font=("Arial", 18, "bold"),
            relief="ridge",
            borderwidth=3
        )
        self.lbl_status.grid(row=0, column=0, sticky="nwe", padx=10, pady=10)
        
        # Button frame
        frm_buttons = tk.Frame(master=self.root, bg="#f0f0f0")
        frm_buttons.rowconfigure(0, weight=1)
        frm_buttons.columnconfigure([0, 1, 2], weight=1)
        
        # Create buttons with images if available
        btn_rock = tk.Button(
            master=frm_buttons,
            text="Rock",
            image=self.images["Rock"],
            compound=tk.TOP,
            font=("Arial", 14, "bold"),
            bg="#ff9a3c",
            activebackground="#ff7b00",
            command=self.play_rock
        )
        btn_rock.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        btn_paper = tk.Button(
            master=frm_buttons,
            text="Paper",
            image=self.images["Paper"],
            compound=tk.TOP,
            font=("Arial", 14, "bold"),
            bg="#3cafff",
            activebackground="#008cff",
            command=self.play_paper
        )
        btn_paper.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        btn_scissors = tk.Button(
            master=frm_buttons,
            text="Scissors",
            image=self.images["Scissors"],
            compound=tk.TOP,
            font=("Arial", 14, "bold"),
            bg="#ff3c3c",
            activebackground="#ff0000",
            command=self.play_scissors
        )
        btn_scissors.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        
        frm_buttons.grid(row=1, column=0, sticky="nsew", padx=10)
        
        # Score frame
        frm_score = tk.Frame(master=self.root, bg="#f0f0f0")
        frm_score.rowconfigure([0, 1], weight=1)
        frm_score.columnconfigure([0, 1], weight=1)
        
        # Score labels
        lbl_player = tk.Label(
            master=frm_score,
            text="Your Score",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 14, "bold"),
            relief="ridge"
        )
        lbl_player.grid(row=0, column=0, sticky="nsew")
        
        lbl_computer = tk.Label(
            master=frm_score,
            text="Computer Score",
            bg="#F44336",
            fg="white",
            font=("Arial", 14, "bold"),
            relief="ridge"
        )
        lbl_computer.grid(row=0, column=1, sticky="nsew")
        
        self.lbl_player_score = tk.Label(
            master=frm_score,
            text="0",
            bg="#8BC34A",
            fg="white",
            font=("Arial", 40, "bold")
        )
        self.lbl_player_score.grid(row=1, column=0, sticky="nsew")
        
        self.lbl_computer_score = tk.Label(
            master=frm_score,
            text="0",
            bg="#FF5722",
            fg="white",
            font=("Arial", 40, "bold")
        )
        self.lbl_computer_score.grid(row=1, column=1, sticky="nsew")
        
        frm_score.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        
        # Reset button
        btn_reset = tk.Button(
            master=self.root,
            text="Reset Game",
            font=("Arial", 16, "bold"),
            bg="#607D8B",
            fg="white",
            activebackground="#455A64",
            command=self.reset_game
        )
        btn_reset.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
    
    def play_rock(self):
        self.play_game(1)
    
    def play_paper(self):
        self.play_game(2)
    
    def play_scissors(self):
        self.play_game(3)
    
    def play_game(self, player_choice):
        computer_choice = randint(1, 3)
        self.lbl_status["text"] = f"Computer chose: {self.choices[computer_choice]}"
        
        # Determine winner
        if player_choice == computer_choice:
            messagebox.showinfo("Result", "It's a tie!")
        elif (player_choice == 1 and computer_choice == 3) or \
             (player_choice == 2 and computer_choice == 1) or \
             (player_choice == 3 and computer_choice == 2):
            self.update_score(self.lbl_player_score)
            messagebox.showinfo("Result", "You win!")
        else:
            self.update_score(self.lbl_computer_score)
            messagebox.showinfo("Result", "Computer wins!")
    
    def update_score(self, label):
        current_score = int(label["text"])
        label["text"] = str(current_score + 1)
    
    def reset_game(self):
        self.lbl_player_score["text"] = "0"
        self.lbl_computer_score["text"] = "0"
        self.lbl_status["text"] = "Make your choice!"

# Create and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()