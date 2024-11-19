from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Configuração do Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # Caminho do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilitar rastreamento de modificações
db = SQLAlchemy(app)

# Definindo o modelo de dados Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Coluna para o ID, chave primária
    nome = db.Column(db.String(150), nullable=False)  # Coluna para o nome
    email = db.Column(db.String(120), unique=True, nullable=False)  # Coluna para o email, único

# Criação da tabela no banco de dados (se ainda não existir)
with app.app_context():
    db.create_all()

# Rota para listar todos os usuários
@app.route('/')
def index():
    usuarios = Usuario.query.all()  # Obtém todos os usuários do banco de dados
    return render_template('index.html', usuarios=usuarios)

# Rota para adicionar um novo usuário
@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    email = request.form['email']
    
    # Criação de um novo objeto Usuario
    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)  # Adiciona o novo usuário à sessão
    db.session.commit()  # Salva no banco de dados
    
    return redirect(url_for('index'))  # Redireciona para a página principal

# Rota para editar um usuário existente
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    usuario = Usuario.query.get_or_404(id)  # Busca o usuário pelo ID
    
    if request.method == 'POST':
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        db.session.commit()  # Salva as alterações no banco de dados
        return redirect(url_for('index'))  # Redireciona para a página principal
    
    return render_template('editar.html', usuario=usuario)  # Exibe o formulário de edição

# Rota para excluir um usuário
@app.route('/excluir/<int:id>')
def excluir(id):
    usuario = Usuario.query.get_or_404(id)  # Busca o usuário pelo ID
    db.session.delete(usuario)  # Deleta o usuário do banco de dados
    db.session.commit()  # Confirma a exclusão
    return redirect(url_for('index'))  # Redireciona para a página principal

if __name__ == '__main__':
    app.run(debug=True)