import os
import urllib.parse

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ['ACCESS_TOKEN_EXPIRE_MINUTES']
REFRESH_TOKEN_EXPIRE_DAYS = os.environ['REFRESH_TOKEN_EXPIRE_DAYS']


SQLALCHEMY_USER = os.environ['SQLALCHEMY_USER']
SQLALCHEMY_PASSWORD = urllib.parse.quote_plus(os.environ['SQLALCHEMY_PASSWORD']).replace('%40', '%%40')
SQLALCHEMY_HOST = os.environ['SQLALCHEMY_HOST']
SQLALCHEMY_PORT = os.environ['SQLALCHEMY_PORT']
SQLALCHEMY_DB = os.environ['SQLALCHEMY_DB']
postgresql_string = 'postgresql+asyncpg://{}:{}@{}:{}/{}'
SQLALCHEMY_DATABASE_URI = postgresql_string.format(SQLALCHEMY_USER, SQLALCHEMY_PASSWORD, SQLALCHEMY_HOST, SQLALCHEMY_PORT, SQLALCHEMY_DB)
