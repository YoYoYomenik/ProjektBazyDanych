import database_instructions as db
import tkinter as tk
from tkinter import ttk

from database_instructions import add_columns

database = 'database.db'
root = tk.Tk()
root.geometry('1200x800')
root.title('Aplikacja-baza danych')


def klik(lbl):
    widok = tk.PanedWindow(root, orient='vertical')
    widok.pack()
    rows = db.printing(database, lbl)
    tree = ttk.Treeview(widok)

#implementacja tabel
    if lbl=='Klienci':
        tree['columns'] = ('kl_id',
                       'kl_nazwa',
                       'kl_adres',
                       'kl_miasto',
                       'kl_woj',
                       'kl_kod',
                       'kl_kraj',
                       'kl_kontakt',
                       'kl_email')
        tree.column('kl_id', width=100, stretch=True)
        tree.column('kl_nazwa', width=150, stretch=True)
        tree.column('kl_adres', width=100, stretch=True)
        tree.column('kl_miasto', width=100, stretch=True)
        tree.column('kl_woj', width=100, stretch=True)
        tree.column('kl_kod', width=100, stretch=True)
        tree.column('kl_kraj', width=100, stretch=True)
        tree.column('kl_kontakt', width=120, stretch=True)
        tree.column('kl_email', width=150, stretch=True)
        tree.heading('kl_id', text='kl_id')
        tree.heading('kl_nazwa', text='kl_nazwa')
        tree.heading('kl_adres', text='kl_adres')
        tree.heading('kl_miasto', text='kl_miasto')
        tree.heading('kl_woj', text='kl_woj')
        tree.heading('kl_kod', text='kl_kod')
        tree.heading('kl_kraj', text='kl_kraj')
        tree.heading('kl_kontakt', text='kl_kontakt')
        tree.heading('kl_email', text='kl_email')
        tree['show'] = 'headings'

    elif lbl=='elementyzamowienia':
        tree['columns']=('zam_numer',
                         'zam_element',
                         'prod_id',
                         'ilosc',
                         'cena_elem')
        tree.column('zam_numer', width=100, stretch=True)
        tree.column('zam_element', width=100, stretch=True)
        tree.column('prod_id', width=100, stretch=True)
        tree.column('ilosc', width=100, stretch=True)
        tree.column('cena_elem', width=100, stretch=True)
        tree.heading('zam_numer', text='zam_numer')
        tree.heading('zam_element', text='zam_element')
        tree.heading('prod_id', text='prod_id')
        tree.heading('ilosc', text='ilosc')
        tree.heading('cena_elem', text='cena_elem')
        tree['show'] = 'headings'

    elif lbl=='zamowienia':
        tree['columns']=('zam_numer',
                         'zam_data',
                         'kl_id')
        tree.column('zam_numer', width=100, stretch=True)
        tree.column('zam_data', width=100, stretch=True)
        tree.column('kl_id', width=100, stretch=True)
        tree.heading('zam_numer', text='zam_numer')
        tree.heading('zam_data', text='zam_data')
        tree.heading('kl_id', text='kl_id')
        tree['show'] = 'headings'

    elif lbl=='Produkty':
        tree['columns']=('prod_id',
                         'dost_id',
                         'prod_nazwa',
                         'prod_cena',
                         'prod_opis')
        tree.column('prod_id', width=100, stretch=True)
        tree.column('dost_id', width=100, stretch=True)
        tree.column('prod_nazwa', width=250, stretch=True)
        tree.column('prod_cena', width=100, stretch=True)
        tree.column('prod_opis', width=400, stretch=True)
        tree.heading('prod_id', text='prod_id')
        tree.heading('dost_id', text='dost_id')
        tree.heading('prod_nazwa', text='prod_nazwa')
        tree.heading('prod_cena', text='prod_cena')
        tree.heading('prod_opis', text='prod_opis')
        tree['show'] = 'headings'

    elif lbl=='Dostawcy':
        tree['columns']=('dost_id',
                         'dost_nazwa',
                         'dost_adres',
                         'dost_miasto',
                         'dost_woj',
                         'dost_kod',
                         'dost_kraj')
        tree.column('dost_id', width=100, stretch=True)
        tree.column('dost_nazwa', width=150, stretch=True)
        tree.column('dost_adres', width=100, stretch=True)
        tree.column('dost_miasto', width=100, stretch=True)
        tree.column('dost_woj', width=100, stretch=True)
        tree.column('dost_kod', width=100, stretch=True)
        tree.column('dost_kraj', width=100, stretch=True)
        tree.heading('dost_id', text='dost_id')
        tree.heading('dost_nazwa', text='dost_nazwa')
        tree.heading('dost_adres', text='dost_adres')
        tree.heading('dost_miasto', text='dost_miasto')
        tree.heading('dost_woj', text='dost_woj')
        tree.heading('dost_kod', text='dost_kod')
        tree.heading('dost_kraj', text='dost_kraj')
        tree['show'] = 'headings'

    scroll = ttk.Scrollbar(tree, orient=tk.VERTICAL)
    tree.configure(yscrollcommand=scroll.set)

    exitt = tk.Button(widok, text='❌', fg='red', height=1, width=2, command=widok.destroy)
    exitt.pack(side='top', anchor='ne', padx=2, pady=2)
    for row in rows:
        # tk.Label(root, text=row).pack()
        tree.insert('', 'end', values=row)
    tree.pack()

def konwersja(text):
    nowy_text=''
    nowy_text=text.get('1.0',tk.END).strip()

    return nowy_text

def sql_command(text):
    zwrot = db.add(database, text)
    columns = add_columns(database, text)

    widok = tk.PanedWindow(root, orient='vertical')
    widok.pack()
    tree = ttk.Treeview(widok)

    tree['columns'] = columns
    tree['show'] = 'headings'

    scroll = ttk.Scrollbar(tree, orient=tk.VERTICAL)
    tree.configure(yscrollcommand=scroll.set)

    exitt = tk.Button(widok, text='❌', fg='red', height=1, width=2, command=widok.destroy)
    exitt.pack(side='top', anchor='ne', padx=2, pady=2)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    for row in zwrot:
        tree.insert('', 'end', values=row)
    tree.pack()


#podział ekranu
top = tk.Frame(root, bg='grey', height=30)
top.pack(fill='x')
left = tk.Frame(root, bg='lightgrey', width=115)
left.pack(side='left', fill='y')
down = tk.Frame(root, bg='white', height=250)
down.pack(side='bottom', fill='x')
sql_text = tk.Text(down, bg='white')
sql_text.pack(side='top', fill='x', padx=5, pady=5)

kl_btn = ttk.Button(root, text="Klienci", command=lambda: klik("Klienci"))
kl_btn.place(x=20, y=200)

elem_zam_btn = ttk.Button(root, text="  Elementy\nzamówienia", command=lambda: klik("elementyzamowienia"))
elem_zam_btn.place(x=20, y=230)

zam_btn = ttk.Button(root, text="Zamówienia", command=lambda: klik("zamowienia"))
zam_btn.place(x=20, y=275)

prod_btn = ttk.Button(root, text="Produkty", command=lambda: klik("Produkty"))
prod_btn.place(x=20, y=305)

dost_btn = ttk.Button(root, text="Dostawcy", command=lambda: klik("Dostawcy"))
dost_btn.place(x=20, y=335)

app_btn = ttk.Button(left, text="Wprowadź\nkomende", command=lambda: sql_command(konwersja(sql_text)))
app_btn.pack(side='bottom', padx=20, pady=30)

'''
1. Raportowanie błędów?
'''


root.mainloop()
