# import modules first Flask, Config=class
from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from flask_migrate import Migrate
from .models import db, login_manager, ma
from .helpers import JSONEncoder
from flask_cors import CORS


#what is the name of the directory thats housing this?

app= Flask(__name__)
app.config.from_object(Config)



app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

db.init_app(app) #need to initate db first, pass the app here

login_manager.init_app(app)
ma.init_app(app)


login_manager.login_view='auth.signin' #specify what page to load for NON-AUTHED users
migrate= Migrate(app, db) #keep track of database changes

app.json_encoder = JSONEncoder

CORS(app)
from .models import User #give me everything else from models after db

