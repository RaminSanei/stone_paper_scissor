import tkinter as tk

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