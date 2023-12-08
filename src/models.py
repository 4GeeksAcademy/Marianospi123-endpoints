from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite = db.relationship("Favorites", backref="user")

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(100), unique=False, nullable=False)
    favorite = db.relationship("Favorites", backref="character")

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    climate = db.Column(db.String(100), unique=False, nullable=False)
    poblation = db.Column(db.String(80), unique=False, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    favorite = db.relationship("Favorites", backref="planets")

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gravity": self.gravity,
            "climate": self.climate,
            "population": self.population,
            "rotation_period": self.rotation_period
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))


    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }