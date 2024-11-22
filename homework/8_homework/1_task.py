class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_data(self):
        print(f" Username: {self.__name} \n Email: {self.__email} \n Password: {self.__password}")

    def set_name(self, name):
        self.__name = name

    def set_email(self, email, ):
        self.__email = email

    def set_password(self, password):
        self.__password = password


user_1 = User("Tom", "tom@gamil.com", "0000")
user_1.get_data()
print("---------------")
user_1.set_name("Tom1")
user_1.set_email("tommm@gamil.com")
user_1.set_password("1111")

user_1.get_data()
