from db import db


class TableItem(db.Model):

    __tablename__ = 'TableItem'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<%r>' % self.title

    def json(self):
        return {
            "id": self.id,
            "date": self.date,
            'title': self.title,
            'distance': self.distance,
            'amount': self.amount
        }