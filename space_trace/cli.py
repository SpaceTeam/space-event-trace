import click
from space_trace import app, db
from space_trace.models import Seat


@app.cli.command("create-db")
def create_seat():
    rows = app.config["SEAT_ROWS"]
    numbers = app.config["SEAT_NUMBERS"]

    # First delete all existing ones
    db.create_all()
    Seat.query.delete()

    # Insert new seats
    for r in range(rows):
        for n in range(numbers):
            db.session.add(Seat(r + 1, n + 1))
    db.session.commit()
    print(f"Added {rows}x{numbers} seats to the database")
