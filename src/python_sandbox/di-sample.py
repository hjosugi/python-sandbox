from abc import ABCMeta, abstractmethod


class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __getitem__(self, key):
        return getattr(self, key)


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass


class DBUserRepository(UserRepository):
    def get_user_by_id(self, user_id):
        user = User(user_id, "John Doe", "")
        return user


class APIUserRepository(UserRepository):
    def get_user_by_id(self, user_id) -> User:
        user = User(user_id, "John Doe", "")
        return user


class Service:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def display_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        print(f"User: {user['name']}")


def main():
    user_repository = APIUserRepository()
    service = Service(user_repository)
    service.display_user(1)


main()
