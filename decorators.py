def introduction(func):
    def inner():
        print("Before execution.")
        func()
        print("After execution")
    return inner


def bye(func):
    def inner():
        func()
        print("Bye!")
    return inner


@introduction
@bye
def hello():
    print("Hello, its executing!")


hello()
