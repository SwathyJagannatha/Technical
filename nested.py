def add():
    x = 15
    def change():
        global x  # Declare x as global to modify it inside the nested function
        x = 20
    print("Before changing:", x)
    print("Making change")
    change()
    print("After changing:", x)

add()
print("Value of x outside:", x)