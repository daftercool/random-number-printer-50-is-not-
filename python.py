import tkinter as tk
import random


def play_game():
    global number
    number = random.randint(1, 100)
    result_label.config(text="picked a number between 1 and 100.\nGuess if it's LOW (≤50) or HIGH (>50).")


def check_guess(guess):
    if number <= 50 and guess == "low":
        result_label.config(text=f" Correct!  {number} (≤ 50).")
    elif number > 50 and guess == "high":
        result_label.config(text=f" Correct!  {number} (> 50).")
    else:
        result_label.config(text=f" Wrong!  {number}. Try again!")


root = tk.Tk()
root.title("Guessing Game ")
root.geometry("400x400")


welcome_label = tk.Label(root, text=" Welcome to My Game!", font=("Arial", 14))
welcome_label.pack(pady=10)

result_label = tk.Label(root, text="'Start Game' to begin!", font=("Arial", 12))
result_label.pack(pady=10)


start_button = tk.Button(root, text="Start Game", command=play_game, font=("Arial", 12))
start_button.pack(pady=5)

low_button = tk.Button(root, text="LOW (≤50)", command=lambda: check_guess("low"), font=("Arial", 12))
low_button.pack(pady=5)

high_button = tk.Button(root, text="HIGH (>50)", command=lambda: check_guess("high"), font=("Arial", 12))
high_button.pack(pady=5)


root.mainloop()











