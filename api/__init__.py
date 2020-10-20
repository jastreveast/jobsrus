from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, static_folder='../dist', static_url_path='/')
    
    # config here 
    # app.config.from_object('config.Config')

    # from .database import db
    # db.init_app(app)
    # migrate = Migrate(app, db)


    with app.app_context():
        # import all parts of the application
        # eg from .home import home 
        from .index import index
        # register blueprints 
        # app.register_blueprint(home.home_bp)
        app.register_blueprint(index.index_bp)

        return app 

