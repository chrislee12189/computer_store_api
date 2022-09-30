from main import ma 
from marshmallow import fields
# from schemas.rating_schema import RatingSchema


class RatingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['rating_id', 'product_id', 'customer_id', 'customer_name', 'product_name', 'rating', 'comment','price']

rating_schema = RatingSchema()
ratings_schema = RatingSchema(many = True)