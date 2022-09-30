from main import ma 
#this import allows us to add length criteria to password validation
from marshmallow.validate import Length


class AdminSchema(ma.Schema):
    class Meta:
        fields = ("admin_id", "username", "email", "password")
    #add validation to admin password
    password = ma.String(validate=Length(min=8, max=30))
    username = ma.String(required = True)
    email = ma.String(required = True)
#this API will only have 1 administrator.
admin_schema = AdminSchema()