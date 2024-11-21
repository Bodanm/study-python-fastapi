class BaseInterface:
    """Base interface"""
    def __init__(self) -> None:
        pass
    def get_attrs(self) -> None:
        pass
    def print_model(self) -> None:
        pass
    def count_of_price(self) -> None:
        pass
    def call_to_support(self) -> None:
        pass

class SiteInterface(BaseInterface):
    """Interface of ouer site"""

    def __init__(self, number, model, price):
        super().__init__()
        self.number =number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of site: {self.model}")

    def count_of_price(self):
        print(f"Count of site price: {self.price ** 2}")

    def call_to_support(self):
        print(f"Number of suppirt is: {self.number}")
        print("You can call from 8 a.m. till 8 p.m.")
class AppInterface(BaseInterface):
    """Interface of ouer App"""

    def __init__(self, number, model, price):
        super().__init__()
        self.number =number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of app: {self.model}")

    def count_of_price(self):
        print(f"Count of app price: {self.price ** 2}")

    def call_to_support(self):
        print(f"Number of suppirt is: {self.number}")
        print("You can call from 8 a.m. till 8 p.m.")


site_user = SiteInterface(12345, "shop",1000 )
app_user = AppInterface(6847465, "android",5000 )

for user in (site_user, app_user):
    user.print_model()
    user.count_of_price()
    user.call_to_support()
    print("--------------")
