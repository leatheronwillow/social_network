from lib.post_repo import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository

    posts = repository.all() # Get all Posts

    # Assert on the results
    assert posts == [
        Post(1, 'LOL', 'Laugh Out Loud', 25, 1),
        Post(2, 'ROFL', 'Rolling on the Floor with Laughter', 10, 2),
        Post(3, 'YOLO', 'you only live okay', 1000, 1),
        Post(4, 'Dunno', "I don't know", 1000, 2)
        ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(3)
    assert post == Post(3, 'YOLO', 'you only live okay', 1000, 1)

"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, "WTF", "What the funk", 250, 2))

    result = repository.all()
    assert result == [
        Post(1, 'LOL', 'Laugh Out Loud', 25, 1),
        Post(2, 'ROFL', 'Rolling on the Floor with Laughter', 10, 2),
        Post(3, 'YOLO', 'you only live okay', 1000, 1),
        Post(4, 'Dunno', "I don't know", 1000, 2),
        Post(5, "WTF", "What the funk", 250, 2)
    ]

"""
When we call PostRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Post(1, 'LOL', 'Laugh Out Loud', 25, 1),
        Post(2, 'ROFL', 'Rolling on the Floor with Laughter', 10, 2),
        Post(4, 'Dunno', "I don't know", 1000, 2),
    ]
