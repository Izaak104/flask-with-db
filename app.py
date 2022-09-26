from flask import Flask, render_template
import sqlite3
import os

#creating a flask app
app = Flask(__name__)

def get_db_connection():
    dir = os.getcwd() + "patients.db"
    print("dir:", dir)
    conn = sqlite3.conne(dir)
    return conn

@app.route("/")
def index():
    conn = get_db_connection
    patientListSql = conn.execute("SELECT * FROM patient_table").fetchall()
    conn()
    print("patientListSql:", patientListSql)
    return render_template("index.html", listPatients=patientListSql)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)


