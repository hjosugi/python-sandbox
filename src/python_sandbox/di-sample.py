class DBUserRepository:
    def get_user_by_id(self, user_id):
        user = {"id": user_id, "name": "John Doe", "email": ""}
        return user


class APIUserRepository:
    def fetch_user_by_id(self, user_id):
        user = {"id": user_id, "name": "John Doe", "email": ""}
        return user


class Service:
    def __init__(self):
        self.user_repository = DBUserRepository()

    def display_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        print(f"User: {user['name']}")


def main():
    service = Service()
    service.display_user(1)


main()
