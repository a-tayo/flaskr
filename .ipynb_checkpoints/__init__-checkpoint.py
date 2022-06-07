# imports
from flask import Flask, jsonify

# controllers
def create_app(test_config=None):
    app = Flask('__name__')
    @app.route('/')
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