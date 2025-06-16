import pandas as pd
from config import DB_PATH
import sqlite3

def export_to_excel():
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query("SELECT * FROM inbox", conn)
    df.to_excel("data/inbox_export.xlsx", index=False)