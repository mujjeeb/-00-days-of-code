from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

DELETE_KEY = "TopSecretAPIKey"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


def initialize_database():
    with app.app_context():
        db.create_all()

# Uncomment the line below when you want to initialize the database
# initialize_database()

def to_dict(self):
    # Method 1.
    dictionary = {}
    # Loop through each column in the data record
    for column in self.__table__.columns:
        # Create a new dictionary entry;
        # where the key is the name of the column
        # and the value is the value of the column
        dictionary[column.name] = getattr(self, column.name)
    return dictionary


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Random route; Returns a random cafe
@app.route("/random", methods=['GET'])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })


# all route; returns all cafes in db
@app.route("/all", methods=['GET'])
def get_all_cafes():
    all_cafes = db.session.query(Cafe).all()
    list_of_cafes = []
    for cafe in all_cafes:
        each_cafe = {"id": cafe.id, "name": cafe.name, "map_url": cafe.map_url, "img_url": cafe.img_url,
                     "location": cafe.location, "has_sockets": cafe.has_sockets, "has_toilet": cafe.has_toilet,
                     "has_wifi": cafe.has_wifi, "can_take_calls": cafe.can_take_calls,
                     "seats": cafe.seats, "coffee_price": cafe.coffee_price
                     }
        list_of_cafes.append(each_cafe)
    cafe_dict = {"cafes": list_of_cafes}

    return jsonify(cafe_dict)

# search route: Returns the searched cafe by location. (?loc=*****)
@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify({"id": cafe.id, "name": cafe.name, "map_url": cafe.map_url, "img_url": cafe.img_url,
                        "location": cafe.location, "has_sockets": cafe.has_sockets, "has_toilet": cafe.has_toilet,
                        "has_wifi": cafe.has_wifi, "can_take_calls": cafe.can_take_calls,
                        "seats": cafe.seats, "coffee_price": cafe.coffee_price
                        })
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    updated_price = request.args.get("new_price")
    all_cafes = db.session.query(Cafe).all()
    for cafe in all_cafes:
        if cafe.id == cafe_id:
            cafe.coffee_price = updated_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated price."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404


@app.route('/report-closed/<cafe_id>', methods=['Delete'])
def delete_cafe(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    api_key = request.args.get('api-key')
    if cafe_to_delete and api_key == DELETE_KEY:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted cafe."})
    elif api_key != DELETE_KEY:
        return jsonify(error={"Forbidden": "Sorry that's not allowed. Make sure you have the correct api_key "}), 403
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database"}), 404





if __name__ == '__main__':
    app.run(debug=True)
