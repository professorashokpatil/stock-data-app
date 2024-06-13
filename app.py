from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_stock():
    serial_number = request.form['serial_number']
    name = request.form['name']
    open_price = request.form['open_price']
    close_price = request.form['close_price']
    high_price = request.form['high_price']
    low_price = request.form['low_price']

    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO stocks (serial_number, name, open_price, close_price, high_price, low_price)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (serial_number, name, open_price, close_price, high_price, low_price))

    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/view')
def view_stocks():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stocks')
    stocks = cursor.fetchall()
    conn.close()
    return render_template('view.html', stocks=stocks)

@app.route('/learn')
def learn():
    return render_template('learn.html')

if __name__ == '__main__':
    app.run(debug=True)
 
