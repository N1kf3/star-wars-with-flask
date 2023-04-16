from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite = db.relationship('Favorite', back_populates="users")

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "favorite": self.favorite
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    favorite = db.relationship('Favorite', back_populates="characters")

    def __repr__(self):
        return 'chatacter %r' %self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "favorite": self.favorite
        }

class Planet(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    favorite = db.relationship('Favorite', back_populates="planets")

    def __repr__(self):
        return 'planet %r' %self.name

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "favorite": self.favorite
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.ForeignKey('character.id'))  
    characters = db.relationship('Favorite', back_populates="character")
    planet_id = db.Column(db.ForeignKey('planet.id'))  
    planets = db.relationship('Favorite', back_populates="planet")
    user_id = db.Column(db.ForeignKey('user.id'))  
    users = db.relationship('User', back_populates="favorite")

    def __repr__(self):
        return 'favorite %r' %self.id
    
    def serialize(self):
        return{
            "id": self.id,
            "character": self.character,
            "planet": self.planet,
            "user": self.user,         
        }

