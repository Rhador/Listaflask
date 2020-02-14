from flask import Flask, render_template, url_for, redirect, request
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    con = sqlite3.connect('tareasBD.db')
    db = con.cursor()
    res = db.execute('SELECT * FROM tareas')

    return render_template('estructura.html', users=res.fetchall())

@app.route('/insert', methods=['POST'])

def insert(): 
    tarea = request.form['texto']   
    con = sqlite3.connect('tareasBD.db')
    db = con.cursor()
    res = db.execute('INSERT INTO tareas (tarea, realizado) VALUES ("%s", 0)' % tarea,)
    con.commit()
    

    return redirect(url_for('home'))


@app.route('/delete/<id>')
def delete(id):
    con = sqlite3.connect('tareasBD.db')
    db = con.cursor()
    res = db.execute('DELETE FROM tareas WHERE id=?', (id,))
    con.commit()
    

    return redirect(url_for('home'))

@app.route('/update/<id>')
def update(id):
    con = sqlite3.connect('tareasBD.db')
    db = con.cursor()
    res = db.execute('UPDATE tareas SET realizado = 1 WHERE id=?', (id,))
    con.commit()

    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)