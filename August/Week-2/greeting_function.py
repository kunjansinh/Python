# Greeting Function


def greet_user(name):
    message = f"Hello, {name}!"
    return message


name = input("Enter your name: ")

greeting = greet_user(name)

print(greeting)