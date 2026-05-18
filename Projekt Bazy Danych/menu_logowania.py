import tkinter as tk
import database_instructions as db
from tkinter import ttk, messagebox

from database_instructions import connect_db


def logowanie(log, pas):
    if connect_db(log, pas):
        pass
    else:
        messagebox.showerror("Error", "Błąd! Niepoprawny login lub hasło!")

def main_window():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Menu logowania SQL")
    #ikona = tk.PhotoImage(file="ikonka.png")
    #root.iconphoto(False, ikona)

    opis_login=tk.Label(root,text="Login:")
    opis_login.pack()
    login=tk.Entry(root)
    login.insert(0, "root")
    login.get()
    login.pack()

    opis_haslo=tk.Label(root,text="Haslo:")
    opis_haslo.pack()
    password = tk.Entry(root)
    password.get()
    password.pack()

    enter=tk.Button(root,text="Zaloguj", command=lambda: logowanie(login, password))
    enter.pack()


    root.mainloop()

main_window()