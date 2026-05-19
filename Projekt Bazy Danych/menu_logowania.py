import tkinter as tk
import database_instructions as db
import main as m
from tkinter import ttk, messagebox
from database_instructions import connect_db


def logowanie(log, pas, bd):
    conn = connect_db(log, pas, bd)
    if conn:
        m.uruchom_aplikacje()
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
    login.pack()

    opis_haslo=tk.Label(root,text="Haslo:")
    opis_haslo.pack()
    password = tk.Entry(root, show="*")
    password.pack()

    opis_bd = tk.Label(root, text="Baza danych:")
    opis_bd.pack()
    bd = tk.Entry(root)
    bd.insert(0, "projekt")
    bd.pack()

    enter=tk.Button(root,text="Zaloguj", command=lambda: logowanie(login.get(), password.get(), bd.get()))
    enter.pack()


    root.mainloop()

main_window()