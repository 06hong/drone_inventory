import os

basedir = os.path.abspath(os.path.dirname(__file__))

#gives access to the project in ANY OS we find ourselves in
#allows outside files/folders to be added to the project from
#the base directory.




class Config:
    SECRET_KEY = "You will never guess..." 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #decrease unncesscary outout in terminal