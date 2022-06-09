# imports
from flask import jsonify, request
from flask_cors import CORS
from models import db, app, Plants

# initialization
db.init_app(app)
cors = CORS(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, DELETE, OPTIONS, PATCH')
    return response


@app.route('/plants', methods=['GET', 'POST'])
def get_plants():
    # implement pagination to display only 10 results at a time
    page = request.args.get('page', 1, type=int)
    start = (page -1)*10
    end = start+10

    # query the plants db to get all plants entries in the db
    plants = Plants.query.all()

    # calls the format method of the Plants class
    formatted_plants = [plant.format() for plant in plants]
    return jsonify({
        'success': True,
        'plants': formatted_plants[start:end],
        'results': len(formatted_plants)
    })

@app.route('/plants/<int:plant_id>')
def get_single_plant(plant_id):
    plant = Plants.query.get_or_404(plant_id)
    return jsonify({
        'success': True,
        'plant': plant.format()
    })

if __name__ == '__main__':
    app.run()