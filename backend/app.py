from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Multi-Service DevOps Application</h1>"

@app.route('/db')
def db():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root123",
            database="devopsdb"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT 'Database Connected Successfully'")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result[0]

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
