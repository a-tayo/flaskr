# imports
from flask import Flask, jsonify
from flask_cors import CORS

# controllers
def create_app(test_config=None):
    app = Flask(__name__)
    cors = CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Headers', 'GET, POST, DELETE, OPTIONS, PATCH')
        return response


    @app.route('/')
    @cross_origin()
    def hello():
        return jsonify({'message': 'Hello World!'})
    
    @app.route('/smiley')
    def smiley():
        return ':)'
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.Environment = 'Development'
    app.run()