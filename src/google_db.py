import sqlite3
from pathlib import Path


DB_Path=Path(__file__).resolve().parents[1]/"data"/"ads.db"

def init_db():

    conn=sqlite3.connect(DB_Path)
    cur=conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS google_ads (
        att1 TEXT,
        att2 INTEGER,
        
    ) 
    """)

    conn.commit()
    conn.close()
    
    
if __name__=="__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")