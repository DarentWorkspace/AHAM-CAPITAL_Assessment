import sqlite3
from models import Fund

DATABASE = 'funds.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS funds (
                fund_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                manager_name TEXT NOT NULL,
                description TEXT NOT NULL,
                nav REAL NOT NULL,
                date_of_creation TEXT NOT NULL,
                performance REAL NOT NULL
            )
        ''')
        conn.commit()

def add_fund(fund):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO funds (name, manager_name, description, nav, date_of_creation, performance)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (fund.name, fund.manager_name, fund.description, fund.nav, fund.date_of_creation, fund.performance))
        conn.commit()

def get_all_funds():
    print("Fetching all funds from the database")
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM funds')
        rows = cursor.fetchall()
        print(f"Rows fetched: {rows}")
        return [Fund(*row) for row in rows]

def get_fund_by_id(fund_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM funds WHERE fund_id = ?', (fund_id,))
        row = cursor.fetchone()
        if row:
            return Fund(*row)
        return None

def update_fund_performance(fund_id, performance):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE funds SET performance = ? WHERE fund_id = ?', (performance, fund_id))
        conn.commit()

def delete_fund(fund_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM funds WHERE fund_id = ?', (fund_id,))
        conn.commit()

def migrate_data():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Write SQL INSERT statements to insert data into the funds table
        cursor.execute('''
            INSERT INTO funds (name, manager_name, description, nav, date_of_creation, performance)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('Test Fund Name', 'Invest Manager', 'Description...', 100, '2024-06-01', 25))
        # Repeat the above statement for each fund to be inserted
        conn.commit()