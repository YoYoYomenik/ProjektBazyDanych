import mysql.connector


def connect_db(us, pas, bd):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user=us.strip(),
            password=pas.strip(),
            database=bd.strip()
        )

        return conn

    except mysql.connector.Error as err:
        print(err)
        return None

def execute_sql(conn, instruction):
    c = conn.cursor()

    try:
        c.execute(instruction)

        # SELECT
        if c.description is not None:

            rows = c.fetchall()
            columns = [col[0] for col in c.description]

            return rows, columns

        # INSERT / UPDATE / DELETE
        else:
            conn.commit()
            return [], []

    except mysql.connector.Error as err:
        print(err)
        return [], []

    finally:
        c.close()


def printing(conn, lb):
    c = conn.cursor()

    try:
        c.execute(f"SELECT * FROM {lb}")
        rows = c.fetchall()
        return rows

    except mysql.connector.Error as err:
        print(err)
        return []

    finally:
        c.close()