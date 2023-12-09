"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from models import db, User, Character, Planets, Favorites
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/character', methods=['POST'])
def create_character():
    data = request.get_json()

    new_character = Character(name=data['name'], eye_color=data['eye_color'], hair_color=data['hair_color'])

    db.session.add(new_character)
    db.session.commit()

    return jsonify({"message": "Character created successfully"}), 201

# Get all characters
@app.route('/characters', methods=['GET'])
def get_all_characters():
    characters = Character.query.all()
    characters_list = [character.serialize() for character in characters]

    return jsonify(characters_list), 200

# Get character by ID
@app.route('/character/<int:character_id>', methods=['GET'])
def get_character_by_id(character_id):
    character = Character.query.get(character_id)

    if character:
        return jsonify(character.serialize()), 200
    else:
        return jsonify({"message": "Character not found"}), 404

# Update character by ID
@app.route('/character/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    character = Character.query.get(character_id)

    if character:
        data = request.get_json()

        character.name = data['name']
        character.eye_color = data['eye_color']
        character.hair_color = data['hair_color']

        db.session.commit()

        return jsonify({"message": "Character updated successfully"}), 200
    else:
        return jsonify({"message": "Character not found"}), 404

# Delete character by ID
@app.route('/character/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Character.query.get(character_id)

    if character:
        db.session.delete(character)
        db.session.commit()

        return jsonify({"message": "Character deleted successfully"}), 200
    else:
        return jsonify({"message": "Character not found"}), 404

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = User(email=data['email'], password=data['password'], is_active=data['is_active'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [user.serialize() for user in users]

    return jsonify(users_list), 200

# Get user by ID
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)

    if user:
        return jsonify(user.serialize()), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Update user by ID
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    if user:
        data = request.get_json()

        user.email = data['email']
        user.password = data['password']
        user.is_active = data['is_active']

        db.session.commit()

        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Delete user by ID
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/planet', methods=['POST'])
def create_planet():
    data = request.get_json()

    new_planet = Planets(
        name=data['name'],
        gravity=data['gravity'],
        climate=data['climate'],
        poblation=data['poblation'],
        rotation_period=data['rotation_period']
    )

    db.session.add(new_planet)
    db.session.commit()

    return jsonify({"message": "Planet created successfully"}), 201

# Get all planets
@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    planets_list = [planet.serialize() for planet in planets]

    return jsonify(planets_list), 200

# Get planet by ID
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = Planets.query.get(planet_id)

    if planet:
        return jsonify(planet.serialize()), 200
    else:
        return jsonify({"message": "Planet not found"}), 404

# Update planet by ID
@app.route('/planet/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    planet = Planets.query.get(planet_id)

    if planet:
        data = request.get_json()

        planet.name = data['name']
        planet.gravity = data['gravity']
        planet.climate = data['climate']
        planet.poblation = data['poblation']
        planet.rotation_period = data['rotation_period']

        db.session.commit()

        return jsonify({"message": "Planet updated successfully"}), 200
    else:
        return jsonify({"message": "Planet not found"}), 404

# Delete planet by ID
@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    planet = Planets.query.get(planet_id)

    if planet:
        db.session.delete(planet)
        db.session.commit()

        return jsonify({"message": "Planet deleted successfully"}), 200
    else:
        return jsonify({"message": "Planet not found"}), 404

# ... (similar endpoints for Favorites)

# Create a new favorite
@app.route('/favorite', methods=['POST'])
def create_favorite():
    data = request.get_json()

    new_favorite = Favorites(
        user_id=data['user_id'],
        planet_id=data['planet_id'],
        character_id=data['character_id']
    )

    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({"message": "Favorite created successfully"}), 201

# Get all favorites
@app.route('/favorites', methods=['GET'])
def get_all_favorites():
    favorites = Favorites.query.all()
    favorites_list = [favorite.serialize() for favorite in favorites]

    return jsonify(favorites_list), 200

# Get favorite by ID
@app.route('/favorite/<int:favorite_id>', methods=['GET'])
def get_favorite_by_id(favorite_id):
    favorite = Favorites.query.get(favorite_id)

    if favorite:
        return jsonify(favorite.serialize()), 200
    else:
        return jsonify({"message": "Favorite not found"}), 404

# Update favorite by ID
@app.route('/favorite/<int:favorite_id>', methods=['PUT'])
def update_favorite(favorite_id):
    favorite = Favorites.query.get(favorite_id)

    if favorite:
        data = request.get_json()

        favorite.user_id = data['user_id']
        favorite.planet_id = data['planet_id']
        favorite.character_id = data['character_id']

        db.session.commit()

        return jsonify({"message": "Favorite updated successfully"}), 200
    else:
        return jsonify({"message": "Favorite not found"}), 404

# Delete favorite by ID
@app.route('/favorite/<int:favorite_id>', methods=['DELETE'])
def delete_favorite(favorite_id):
    favorite = Favorites.query.get(favorite_id)

    if favorite:
        db.session.delete(favorite)
        db.session.commit()

        return jsonify({"message": "Favorite deleted successfully"}), 200
    else:
        return jsonify({"message": "Favorite not found"}), 404


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 4478))
    app.run(host='0.0.0.0', port=PORT, debug=False)

