from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria um API flask
app = Flask(__name__)

# Cria uma instância SQLAlchemy
app.config['SECRET_KEY'] = 'FSD2323f#!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

# Cria conexão BD
db = SQLAlchemy(app)
db:SQLAlchemy # Mostra o tipo da variável, no caso SQLAlchemy

#Definir estrutura do BD por meio da classe db.Model
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem', backref='autor') #define relacionamento entre membros da classe
    
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor')) #define relacionamento entre membros da classe



# Criar usuários admins
autor = Autor(nome='Daniel', email='danielbruno84@gamil.com', senha='123456', admin=True)

# Executa para zerar e criar/recriar Banco de Dados
def inicializar_db():
    with  app.app_context():
        # Executar o comando para criar banco de dados
        db.drop_all()
        db.create_all()
        #Criar usuário administrador
        autor = Autor(nome='Daniel', email='danielbruno84@gamil.com', senha='123456', admin=True) 
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    inicializar_db()