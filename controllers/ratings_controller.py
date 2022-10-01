from flask import Blueprint 
from flask import jsonify
from models.ratings import Ratings
from schemas.rating_schema import ratings_schema, rating_schema
from marshmallow.exceptions import ValidationError



rating = Blueprint('rating', __name__, url_prefix='/ratings')

# GET ratings, this is inteded to be GET only. In future, POSTING a rating is intended to be only accessible to customers who have an order ID. I dont have time for that at the moment, so it will be added as a feature for future versions.

@rating.route('/', methods = ['GET'])
def get_ratings():
    rating_list = Ratings.query.all()
    result =  ratings_schema.dump(rating_list)
    return jsonify(result)

@rating.route('/<int:id>', methods = ['GET'])
def find_ratings_by_id(id):
    rating = Ratings.query.get(id)
    if not rating:
        return {"Error": "No such rating was found, please check the rating ID and try again."}, 404
    result = rating_schema.dump(rating)
    return jsonify(result)




@rating.errorhandler(ValidationError)
def register_validation_errors(error):
    return error.messages, 400


#! RATINGS IS A GOOD OBJECT TO PRACTISE QUERY STRINGS ON