class A:
    """Class A"""
    name_a = "class A is parent"
    is_main_class =True

    def print_hello(self):
        print("Hello from A")
class B(A):
    """Class B"""
    name_b = "class B is a child"
    is_main_class = False

    def print_hello(self):
        print("Hello from B")

class C(B):
    """Class C"""
    pass

test_ex = C()
print(test_ex.name_a)
print(test_ex.name_b)
print(test_ex.is_main_class)

test_ex.print_hello()