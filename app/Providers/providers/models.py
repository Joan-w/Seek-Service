from providers import db

class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    phone_number = db.Column(db.String(12), unique=True)
    county = db.Column(db.String(20), nullable=False)
    specialty = db.Column(db.String(20), nullable=False)
    bio = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Provider('{self.username}', '{self.email}', '{self.specialty}', '{self.image_file}')"
