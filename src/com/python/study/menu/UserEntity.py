class UserEntity:

    def __init__(self, username, password, name, email):
self.username = username
self.password = password
self.name = name
self.email = email

def__str__(self):
return f"[UserEntity]: username: {self.username},
password: {self.password}, name: {self.name},
email: {self.email}"