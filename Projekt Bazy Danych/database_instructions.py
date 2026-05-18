import mysql.connector

def connect_db(db):
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="TWOJE_HASLO",
        #database=db
    )

# potrzebne raz, przy tworzeniu bazy danych
def create(db):
    conn = connect_db(db)
    c = conn.cursor()

    tworzenie = open('tworzenie.txt', 'r', encoding='utf-16-le')
    dodawanie = open('wypelnianie.txt', 'r', encoding='utf-8')
    caly_tekst = tworzenie.read()

    c.execute(caly_tekst)
    caly_tekst = dodawanie.read()

    c.execute(caly_tekst)
    conn.commit()

    tworzenie.close()
    dodawanie.close()
    c.close()
    conn.close()


def add(db, instruction):
    conn = connect_db(db)
    c = conn.cursor()

    c.execute(instruction) #wykonuje jedną instrukcję
    rows = c.fetchall()
    columns = [col[0] for col in c.description]

    conn.close()
    return list(rows)

def add_columns(db, instruction):
    conn = connect_db(db)
    c = conn.cursor()
    c.execute(instruction)  # wykonuje jedną instrukcję
    rows = c.fetchall()
    columns = [col[0] for col in c.description]
    conn.close()
    return columns

def printing(db, lb):
    conn = connect_db(db)
    c = conn.cursor()

    c.execute(f"SELECT * FROM {lb}")
    rows = c.fetchall()

    conn.close()
    return list(rows)