from lib.user_repo import UserRepository
from lib.users import User

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() # Get all Users

    # Assert on the results
    assert users == [
        User(1, "m.h.azad-14@outlook.com", "batpadman"),
        User(2, "f.p.ghouri@yahoo.com", "leatheronwillow")
    ]

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, "f.p.ghouri@yahoo.com", "leatheronwillow")

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "imran.azad@ymail.com", "baba"))

    result = repository.all()
    assert result == [
        User(1, "m.h.azad-14@outlook.com", "batpadman"),
        User(2, "f.p.ghouri@yahoo.com", "leatheronwillow"),
        User(3, "imran.azad@ymail.com", "baba")
    ]

"""
When we call UserRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(2) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        User(1, "m.h.azad-14@outlook.com", "batpadman"),
    ]
