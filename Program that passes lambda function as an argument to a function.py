def func(f, n):
    print(f(n))
    
    twice = lambda x: x*2
    thrice = lambda x: x*3
    
    func(twice, 4)
    func(thrice, 3)