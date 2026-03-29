import sqlite3

DATABASE="database_income.db"

def create_jobs_table():
    con=sqlite3.connect(DATABASE)
    con.execute("""
                CREATE TABLE IF NOT EXISTS jobs 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                yph NUMBER
                )
                """)
    con.close()

def create_worktimes_table():
    con=sqlite3.connect(DATABASE)
    con.execute("""
                CREATE TABLE IF NOT EXISTS worktimes 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER,
                time NUMBER,
                year NUMBER,
                month NUMBER,
                day NUMBER,
                hour NUMBER,
                minute NUMBER
                )
                """)
    con.close()