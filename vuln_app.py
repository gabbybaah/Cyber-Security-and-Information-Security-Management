from flask import Flask, request
import sqlite3
app = Flask(__name__)

@app.route("/portal")
def portal():
    uid = request.args.get("id", "1")
    conn = sqlite3.connect("erp_portal.db")
    query = f"SELECT * FROM credentials WHERE rowid = {uid}"
    result = conn.execute(query).fetchall()
    return str(result)

app.run(host="127.0.0.1", port=5000)
