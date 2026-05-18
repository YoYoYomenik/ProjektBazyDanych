import tkinter as tk
from tkinter import ttk

def main_window():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Menu logowania")
    #ikona = tk.PhotoImage(file="ikonka.png")
    #root.iconphoto(False, ikona)

    login =tk.Entry(root)
    login.pack()
    password = tk.Entry(root)
    password.pack()


    root.mainloop()

main_window()