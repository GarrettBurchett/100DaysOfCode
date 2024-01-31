import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:    
        try:
            with open("Day29/data.json", mode='r') as file:
                data = json.load(file) # Reading old data
        except FileNotFoundError:
            with open("Day29/data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)    
        else:
            data.update(new_data) # Updating old data with new data
            with open("Day29/data.json", mode='w') as file:
                json.dump(data, file, indent=4) # Saving updated data
        finally:    
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ----------------- Search For Website Credentials -------------------- # 
def find_credentials():
    website = website_entry.get()
    try:
        with open("Day29/data.json", mode='r') as file:
                data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Search Error", message="You don't have any credentials saved with this app.")
    else:
        try:
            username = data[website]['username']
            password = data[website]['password']
        except KeyError as ke:
            messagebox.showerror(title="Search Error", message=f"You don't have any credientials saved for {ke}")
        else:
            messagebox.showinfo(title=f"{website} Credentials", message=f"Username: {username}\nPassword: {password}")
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
#window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_pic = tk.PhotoImage(file='Day29/logo.png')
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(column=1, row=0)

website_title = tk.Label(text="Website:")
website_title.grid(column=0, row=1)

website_entry = tk.Entry(width=21)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

search_button = tk.Button(text="Search", command=find_credentials)
search_button.grid(column=2, row=1, sticky="EW")

email_username_title = tk.Label(text="Email/Username:")
email_username_title.grid(column=0, row=2)

email_username_entry = tk.Entry(width=35)
email_username_entry.insert(0, "someone@email.com")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_title = tk.Label(text="Password:")
password_title.grid(column=0, row=3)

password_entry = tk.Entry(width=21) # , show='*'
password_entry.grid(column=1, row=3, sticky="EW")

password_button = tk.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()