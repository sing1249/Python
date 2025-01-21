import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean



app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def dictionary_convert(self):
    #Using dictionary comprehension to conver the table data into dict
        return {each.name: getattr(self, each.name) for each in self.__table__.columns}



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/random")
def random_cafe():
    with app.app_context():
        all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
        random_cafe = random.choice(all_cafes)
        return jsonify(cafe=random_cafe.dictionary_convert())

@app.route("/london")
def london_cafes():
    with app.app_context():
        london_cafes = db.session.execute(db.select(Cafe)).scalars().all() #Returns a list
        #To convert all cafes into dict format, used list comprehension and jsonify on each item
        return jsonify(cafe=[cafes.dictionary_convert() for cafes in london_cafes])

#>> > stmt = select(User).where(User.name == "spongebob")
@app.route("/search")
def search_cafe():
    with app.app_context():
        requested_location = request.args.get('loc') #Gets hold of the users parameter passed in URL
        searched_cafe = db.session.execute(db.select(Cafe).where(Cafe.location == requested_location)).scalars().all() #Finds the loc in db
        if searched_cafe:
            return jsonify(cafe=[found_cafe.dictionary_convert() for found_cafe in searched_cafe])
        else:
            return jsonify(error={"Not Found": "Sorry, No cafe found at this location"}), 404
        #
        # {
        #     "id": random_cafe.id,
        #     "name": random_cafe.name,
        #     "map_link": random_cafe.map_url,
        #     "image": random_cafe.img_url,
        #     "location": random_cafe.location,
        #     "sockets": random_cafe.has_sockets,
        #     "toilets": random_cafe.has_toilet,
        #     "can take calls": random_cafe.can_take_calls,
        #     "seats": random_cafe.seats,
        #     "coffee price": random_cafe.coffee_price,
        # }


# HTTP POST - Create Record
@app.route("/add", methods=['POST', 'GET'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "New Cafe Added!"})

# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get("new_price") #User will write the new_price and getting hold of that.
    cafe = db.get_or_404(Cafe, cafe_id) #Getting hold of the cafe with id that user wrote from the Cafe db.
    if cafe: #If cafe is found then:
        cafe.coffee_price = new_price
        db.session.commit() #changes the coffee price to the new coffee price
        return jsonify(response={"New Coffee Price": "Updated"})
    else:
        return jsonify(error={"Error": "Could not find the cafe with that id"}), 200



# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key") #Checks for what the API key is given by user
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Cafe Deleted": "The Cafe has been deleted from the database!"}), 200
        else:
            return jsonify(error={"No Cafe found": "Cafe with that ID can not be found"}), 200
    else:
        return jsonify(error={"No Acess": "The API key provided is invalid"}), 403


if __name__ == '__main__':
    app.run(debug=True)
