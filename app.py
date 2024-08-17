from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Conexão com o banco de dados
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Criação da tabela de usuários
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )''')
conn.commit()


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_username = data['username']
    new_password = data['password']

    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (new_username, new_password))
        conn.commit()
        session['username'] = new_username
        return redirect(url_for('dashboard'))
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'message': 'Nome de usuário já existe.'})


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return jsonify({'success': False, 'message': 'Nome de usuário ou senha incorretos.'})


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
