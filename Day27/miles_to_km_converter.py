import tkinter as tk

def convert_mi_to_km():
    miles = float(entry.get())
    converted_label.config(text=f"{miles * 1.609}")

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

entry = tk.Entry(width=15)
entry.grid(column=1, row=0)

equals_label = tk.Label(text="is equal to")
equals_label.grid(column=0, row=1)

converted_label = tk.Label()
converted_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=convert_mi_to_km)
button.grid(column=1, row=2)

window.mainloop()
