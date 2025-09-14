import tkinter
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Information", "This is a message box")
    
    label = tkinter.Label(text="Hello, Tkinter!")
    label.pack(pady=100, padx=100)
root = tkinter.Tk()
root.title("Tkinter Example")

button = tkinter.Button(root, text="Show Message", command=show_message)
button.pack(pady=20, padx=20)

root.mainloop()