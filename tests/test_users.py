from lib.users import User

"""
User constructs with an id, email and username
"""
def test_user_constructs():
    user = User(1, "m.h.azad-14@outlook.com", "batpadman")
    assert user.id == 1
    assert user.email == "m.h.azad-14@outlook.com"
    assert user.username == "batpadman"

"""
We can format Users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "m.h.azad-14@outlook.com", "batpadman")
    assert str(user) == "User(1, m.h.azad-14@outlook.com, batpadman)"

"""
We can compare two identical Users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "m.h.azad-14@outlook.com", "batpadman")
    user2 = User(1, "m.h.azad-14@outlook.com", "batpadman")
    assert user1 == user2
   