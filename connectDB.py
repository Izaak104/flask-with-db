import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect("patients.db")
    conn.row_factory = sqlite3.Row
    return conn

db = get_db_connection()
patientListSql = db.execute("SELECT * FROM patient_table").fetchall()
patientListSql

##save data to dataframe
df = pd.DataFrame(patientListSql)
df

##renaming columns
df.columns = ["idnumber", "sex", "email", "phonenumber"]
df

