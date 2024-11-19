def say_hello(username, age):
    print(f"Hello {username}, welcom to the club, buddy!")
    print(f"Your age is {age}, you are so beautiful!")
    print("-------------------------")


def print_numbers(start, stop):
    for num in range(start, stop):
        print(f"Current num is: {num}")
    print("------------------")

user_data = {
    "Dima": 25,
    "Sara": 34,
    "Tom": 11}
list_of_ranges = [(1, 10), (2, 9), (0, 100)]

# for name, age in user_data.items():
#     say_hello(name, age)


for start_pos, stop_pos in list_of_ranges:
    print_numbers(start_pos, stop_pos)
