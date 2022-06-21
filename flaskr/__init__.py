from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
    app.config['SECRET_KEY'] = 'secret'

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')

    return app
