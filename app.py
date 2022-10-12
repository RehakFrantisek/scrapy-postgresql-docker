import psycopg2
from flask import Flask, render_template

app = Flask(__name__)


def get_connection():
    conn = psycopg2.connect(
        host='postgres',
        database='postgres',
        user='postgres',
        password='postgres'
    )
    return conn


@app.route('/')
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM srealitydata')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
