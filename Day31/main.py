import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    quiz_words = pd.read_csv("Day31/data/words_to_learn.csv")
except FileNotFoundError:
    quiz_words = pd.read_csv("Day31/data/french_words.csv")

words_dict = quiz_words.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(background, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card['French'], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(background, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")

def already_know():
    words_dict.remove(current_card)
    data = pd.DataFrame(words_dict)
    data.to_csv("Day31/data/words_to_learn.csv", index=False)
    next_card()

window = tk.Tk()
window.title("Flashy Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

wrong_pic = tk.PhotoImage(file="Day31/images/wrong.png")
right_pic = tk.PhotoImage(file="Day31/images/right.png")
card_front = tk.PhotoImage(file="Day31/images/card_front.png")
card_back = tk.PhotoImage(file="Day31/images/card_back.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_button = tk.Button(image=wrong_pic, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

check_button = tk.Button(image=right_pic, highlightthickness=0, command=already_know)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()