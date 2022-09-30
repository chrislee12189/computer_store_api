from main import ma 



class RatingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ['rating_id', 'product_id', 'customer_id', 'customer_name', 'product_name', 'rating', 'comment','price']

rating_schema = RatingSchema()
ratings_schema = RatingSchema(many = True)