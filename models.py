from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class News(db.Model):
  __tablename__ = 'news'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(500), nullable=False)
  excerpt = db.Column(db.String(500), nullable=False)
  reference = db.Column(db.String(), nullable=False)
  keyword = db.Column(db.String(10), nullable=False) 
  frequency = db.Column(db.Integer(), nullable=False)

  def __init__(self, keyword="" ,frequency=0):
    self.key = keyword
    self.freq = frequency
    
  @classmethod
  def create(cls, title, excerpt, reference, keyword, frequency):
    new = News(
      title=title, 
      excerpt=excerpt, 
      reference=reference,
      keyword=keyword, 
      frequency=frequency
    )
    
    return new.save()
  
  def save(self):
    try:
      db.session.add(self)
      db.session.commit()
      return self
    except:
      return False

def json(self):
  return {'reference': self.reference}

