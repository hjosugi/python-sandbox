from abc import ABCMeta, abstractmethod
import requests


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass


class DBUserRepository(UserRepository):
    def __init__(self, db_con):
        self.db_con = db_con

    def get_user_by_id(self, user_id):
        cur = self.db_con.cursor()
        cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cur.fetchone()
        return user


class APIUserRepository(UserRepository):
    def __init__(self, url):
        self.url = url

    def get_user_by_id(self, user_id):
        res = requests.get(f"{self.url}/user/{user_id}")
        user = res.json()
        return user


class Service:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def display_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        print(f"User: {user['name']}")


def main():
    user_repository = APIUserRepository("http://127.0.0.1:5000")
    service = Service(user_repository)
    service.display_user(2)


main()
