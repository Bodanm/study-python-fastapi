class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def update_name(self, new_name):
        self.name = new_name

    def update_balance(self, new_balance):
        self.balance = new_balance

    def get_user_info(self):
        return {"name": self.name, "balance": self.balance}

    def remove_user(self):
        print(f"{self.name} has been deleted")
        self.name = None
        self.balance = None



user_1 = User("Tom", 1000)
user_2 = User("Jake", 2000)

print(user_1.get_user_info())
print(user_2.get_user_info())

user_1.update_name("Tomek")
user_2.update_balance(200)

print("\nAfter updating:")
print(user_1.get_user_info())
print(user_2.get_user_info())

user_3 = User("Tom", 1000)
print(user_3.get_user_info())
user_3.remove_user()
print(user_3.get_user_info())


