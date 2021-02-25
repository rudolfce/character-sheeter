from sheeter.database import db


class User(db.Model):
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    _is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.Integer)
    authenticated = db.Column(db.Boolean, default=False)

    @property
    def is_active(self):
        """True, as all users are active."""
        return self._is_active

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
