import psycopg2

class Config:
  pass

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'postgresql://jessicavilla@localhost/newsdb'
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
  'development': DevelopmentConfig,
}