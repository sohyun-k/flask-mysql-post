from db_connect import db
from datetime import datetime

class Post(db.Model):
    __tablename__='post'
    id = db.Column(db.Integer, primary_key = True, nullable=False, autoincrement = True)
    author = db.Column(db.String(256), nullable=False)
    title = db.Column(db.Text(), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    like = db.Column(db.Integer, default = 0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    isAnonymous = db.Column(db.Integer, nullable=False)

    def __init__(self, author, title, content, isAnonymous):
        self.author = author
        self.title = title
        self.content = content
        self.isAnonymous = isAnonymous
    
    #Post('sohyun', 'hello')
