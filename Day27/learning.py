import tkinter as tk

def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)

# Initializes the GUI window
window = tk.Tk()
window.title("My First GUI Program")
# Sets the minimum size of the window, or how big the window is upon first running the program. Can adjust size manually after running
window.minsize(width=500, height=500)
# Padding adds extra space around the object, in this case the whole window.
window.config(padx=20, pady=20)

# Label
my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold")) # The 3rd argument in font is optional.
# Ways to change the value of keyword args. Both options return the same result.
my_label["text"] = "New Text"
my_label.config(text="New Text")
#my_label.pack() # This method automatically puts the label on the screen and centers it.
#my_label.place(x=0, y=0) # Place is used for precise layout by putting the object at that specific coordinate.
my_label.grid(column=0, row=0) # If no other widgets, then the column and row values won't matter and put object in top left corner
my_label.config(padx=50, pady=50) # Creates padding around the label widget only.

# Button
button = tk.Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)

# Entry
entry = tk.Entry(width=10)
entry.insert(tk.END, string="Some text to begin with")
entry.get()
#entry.pack()
entry.grid(column=3, row=2)

new_button = tk.Button(text="No Click Me")
new_button.grid(column=2, row=0)


# # Text box
# text = tk.Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(tk.END, "Example of multi-line text entry.")
# print(text.get("1.0", tk.END))
# text.pack()

# # Spinbox
# def spinbox_used():
#     print(spinbox.get())
# spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = tk.Scale(from_=0, to=100, command=scale_used)
# scale.pack()

# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = tk.IntVar()
# checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# # Radiobutton
# def radio_used():
#     print(radio_state.get())
# # Variable to hold on to which radio button value is checked.
# radio_state = tk.IntVar()
# radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))

# listbox = tk.Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# Keeps the window running, similar to a while True loop. Goes at the very end of your program (all functionality goes before)
window.mainloop()
