from datetime import date, datetime
from enum import unique
from space_trace import db, app


class User(db.Model):
    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.Text, nullable=False)
    email: str = db.Column(db.Text, unique=True, nullable=False)
    created_at: datetime = db.Column(
        db.DateTime, nullable=False, default=db.func.now()
    )
    vaccinated_till: date = db.Column(db.Date, nullable=True, default=None)

    __table_args__ = (db.Index("idx_users_email", email),)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def is_admin(self) -> bool:
        return self.email in app.config["ADMINS"]

    def first_name(self) -> str:
        first, _ = self.email.split("@")[0].split(".")
        first = first.capitalize()
        first = "-".join(map(lambda n: n[0].upper() + n[1:], first.split("-")))
        return first

    def last_name(self) -> str:
        _, last = self.email.split("@")[0].split(".")
        last = last.capitalize()
        last = "-".join(map(lambda n: n[0].upper() + n[1:], last.split("-")))
        return last

    def full_name(self) -> str:
        first, last = self.email.split("@")[0].split(".")
        name = first.capitalize() + " " + last.capitalize()
        name = "-".join(map(lambda n: n[0].upper() + n[1:], name.split("-")))
        return name

    def is_vaccinated(self) -> bool:
        return (
            self.vaccinated_till is not None
            and self.vaccinated_till >= date.today()
        )

    def __repr__(self):
        return f"<User id={self.id}, name={self.name}, email={self.email}>"


class Visit(db.Model):
    __tablename__ = "visits"
    id: int = db.Column(db.Integer, primary_key=True)
    user: int = db.Column(db.ForeignKey("users.id"), nullable=False)
    timestamp: datetime = db.Column(
        db.DateTime, nullable=False, default=db.func.now()
    )

    __table_args__ = (db.Index("idx_visits_user", user),)

    def __init__(self, timestamp: datetime, user_id: int):
        self.timestamp = timestamp
        self.user = user_id

    def __repr__(self):
        return (
            f"<Visit id={self.id}, userId={self.user}, "
            "timestamp={self.timestamp}>"
        )


class Seat(db.Model):
    __tablename__ = "seats"
    id: int = db.Column(db.Integer, primary_key=True)
    user: int = db.Column(
        db.ForeignKey("users.id"), nullable=True, unique=True
    )
    row: int = db.Column(db.Integer, nullable=False)
    number: int = db.Column(db.Integer, nullable=False)

    __table_args__ = (db.Index("idx_seats_user", user),)

    def __init__(self, row: int, number: int):
        self.row = row
        self.number = number

    def __repr__(self):
        return f"<Seat id={self.id}, userId={self.user}, row={self.row}, number={self.number} >"
