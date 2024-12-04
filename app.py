import psycopg2
from psycopg2 import sql
import bcrypt
from flask import Flask, render_template, request

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'ep-sweet-moon-a5s30lhj.us-east-2.aws.neon.tech',
    'dbname': 'diario_estudo_db',
    'user': 'diario_estudo_db_owner',
    'password': 'kWvHnU9L0NPV',
    'port': 5432
}

# Testando a conexão com o banco de dados
try:
    conn = psycopg2.connect(**db_config)
    print("Conexão bem-sucedida com o banco de dados!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Rota de Registro de Usuário
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome_usuario = request.form['nome_usuario']
        senha = request.form['senha']

        # Criptografar a senha
        hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        try:
            # Conectar ao banco de dados
            conn = psycopg2.connect(**db_config)
            cursor = conn.cursor()

            # Verificar se o nome de usuário já existe
            cursor.execute(
                "SELECT * FROM usuarios WHERE nome_usuario = %s",
                (nome_usuario,)
            )
            if cursor.fetchone():
                cursor.close()
                conn.close()
                return "Nome de usuário já existe."

            # Inserir o novo usuário
            cursor.execute(
                "INSERT INTO usuarios (nome_usuario, senha) VALUES (%s, %s)",
                (nome_usuario, hashed_password.decode('utf-8'))
            )
            conn.commit()

            cursor.close()
            conn.close()

            return "Registrado com sucesso! Aqui inicia a sua jornada pelo Japão!"
        except Exception as e:
            return f"Erro ao registrar o usuário: {e}"

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
