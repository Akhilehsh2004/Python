def outer_func():
    var = 10
    def inner_func():
        var = 20
        print("Inner Variable = ", var)
    inner_func()
    print("Outer Variable = ", var)
outer_func()