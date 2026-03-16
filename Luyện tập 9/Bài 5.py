class User:
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
            return self._id


u = User(10574)
print("User ID:", u.id )