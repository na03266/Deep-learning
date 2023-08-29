from model.user import User

class AuthenticationController:
    def __init__(self):
        self.registered_users = []

    def register_user(self, username, password):
        user = User(username, password)
        self.registered_users.append(user)
        return user

    def authenticate_user(self, username, password):
        for user in self.registered_users:
            if user.username == username and user.password == password:
                return True
        return False
