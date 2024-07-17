import os
from urllib.parse import quote

class Config:
    password = 'lvq0612@'
    encoded_password = quote(password)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'mysql+pymysql://root:{encoded_password}@localhost/comicbooks_reading')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
