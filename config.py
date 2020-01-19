from pathlib import Path
import os
import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

root_path = Path(__file__).parent
connexion_app = connexion.App(__name__, specification_dir=root_path)
app = connexion_app.app

app.config['SQLALCHEMY_ECHO'] = True  # for debug TODO remove later
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steam.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
