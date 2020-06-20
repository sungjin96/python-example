# s = "GLOBAL VARIABLE!"


# def func():
#     mylocal = 10
#     # print(locals())
#     print(globals()['s'])
# func()


# def hello(name="Jose"):
#     return "hello"+name


# print(hello())
# mynewgreet = hello

# print(mynewgreet())

def hello(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GEER()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"
    print(greet())
    print(welcome())
    print("End of hello()")

hello()
