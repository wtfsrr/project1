import tkinter as tk

window = tk.Tk()
window.title("Планы")
window.geometry("800x600")
window["bg"] = "black"

label = tk.Label(window, text="Привет, это мой проект!",
                 font=("Arial", 20, "bold"), fg="white", bg="black")
label.pack(expand=True)

window.mainloop()