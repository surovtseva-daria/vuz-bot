from flask import Flask, request, jsonify, Blueprint
from calculator import calculator

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/vuzes/')
def vuzes():
    rus = request.args.get('rus')
    math = request.args.get('math')
    obsh = request.args.get('obsh')
    foreg = request.args.get('foreg')
    inform = request.args.get('inform')
    biolog = request.args.get('biolog')
    geog = request.args.get('geog')
    xim = request.args.get('xim')
    fiz = request.args.get('fiz')
    lit = request.args.get('lit')
    hist = request.args.get('hist')
    limit = request.args.get('limit', default=100)
    region = request.args.get('region', default='')
    dopexam = request.args.get('dopexam', default=0)
    return jsonify(calculator(rus=rus, math=math, obsh=obsh,
                              foreg=foreg, inform=inform, biolog=biolog, geog=geog,
                              xim=xim, fiz=fiz, lit=lit, hist=hist, limit=limit, region=region,dopexam=dopexam))


errors = Blueprint('errors', __name__)


@errors.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code


if __name__ == '__main__':
    app.run(debug=True)
