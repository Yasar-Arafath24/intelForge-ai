from app.db.database import engine


def test_connection():

    connection = engine.connect()

    assert connection

    connection.close()