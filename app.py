from flask import Flask
from flasgger import Swagger
from api.route import home_route, sheet_route

def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'Geração de Folha de Frequência',
    }

    swagger = Swagger(app)

    app.register_blueprint(home_route.home_api, url_prefix='/api')
    app.register_blueprint(sheet_route.sheet_api, url_prefix='/api/sheet')

    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=500, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)