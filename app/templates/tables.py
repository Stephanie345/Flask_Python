from app import db

class Transacao(db.Model):
    __tablename__ = "transacoes"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String)
    valor = db.Column(db.Float)
    data = db.Column(db.DateTime)

    def __init__(self, descricao, valor, data):
        self.descricao = descricao
        self.valor = valor
        self.data = data

    def __repr__(self):
        return "<Transacao %r>" % self.id