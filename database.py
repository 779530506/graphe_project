
# import os
# import flask

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
import pandas as pd
def getData():
    d = pd.read_json("/home/abdoulayesarr/Documents/MasterBigdata/analyse_reseaux_sociaux/avocado_analytics/villes.json")
    print(d)
# def initDB():
#     server = flask.Flask(__name__)



#     server.config['SECRET_KEY'] = 'mysecretkey'
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
#     server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db = SQLAlchemy(server)

    
        
#     Migrate(server,db)
    # class User(db.Model):
    #     id = db.Column(db.Integer, primary_key=True)
    #     username = db.Column(db.String, unique=True, nullable=False)
    #     email = db.Column(db.String)
    # with server.app_context():
    #     db.create_all()

#     return server,db

    