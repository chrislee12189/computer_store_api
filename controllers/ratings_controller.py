from flask import Blueprint 
from flask import jsonify
from models.ratings import Ratings
from schemas.rating_schema import ratings_schema




rating = Blueprint('rating', __name__, url_prefix='/ratings')

# GET ratings 

@rating.route('/', methods = ['GET'])
def get_ratings():
    rating_list = Ratings.query.all()
    result =  ratings_schema.dump(rating_list)
    return jsonify(result)