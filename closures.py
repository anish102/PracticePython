def outerFunc(name):
    def innerFunc():
        print(f'Hello, {name}')
    return innerFunc


x = outerFunc("Sam")
x()
