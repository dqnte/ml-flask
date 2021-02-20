from .. import db, flask_bcrypt


class User(db.Model):
    # User Model Data
    __tablename__ = "user"

    # Identification Properties
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    public_id = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))

    # Contact Information
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, unique=False, nullable=True)
    first_name = db.Column(db.String(50, unique=False, nullable=False))
    last_name = db.Column(db.String(50, unique=False, nullable=False))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
