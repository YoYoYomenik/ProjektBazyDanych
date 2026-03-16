import database_instructions as db
import tkinter as tk
from tkinter import ttk

database = 'database.db'
root = tk.Tk()
root.geometry('600x400')
root.title('Tytuł')

kl_btn = ttk.Button(root, text="Klienci")
kl_btn.pack()

'''
1. Zrobić przyciski tabel
2. Po naciśnięciu przycików, wyświetla się tabela
3. Dodać miejsce na pisanie kodu w SQl-u
'''

rows = db.printing(database, "Klienci")
tree = ttk.Treeview(root)
tree['columns'] = ['kl_id',
  'kl_nazwa',
  'kl_adres',
  'kl_miasto',
  'kl_woj',
  'kl_kod',
  'kl_kraj',
  'kl_kontakt',
  'kl_email']

for row in rows:
    #tk.Label(root, text=row).pack()
    tree.insert('', 'end', values=row)
    tree.pack()


root.mainloop()
