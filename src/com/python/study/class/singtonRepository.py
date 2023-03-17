class stingLtonRepository:
....instance = None

....@classmethod
....def getInstance(cls):
.........if cls.instance == None:
........cls.instance = stingLtonRepository()
........return cls.instance

....def __init__(self):
........self.userList = List()


