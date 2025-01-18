print((lambda n: n*n*n)(3))
print((lambda x,y,z: (x+y+z)/3)(10,20,30))
print((lambda s:s.lstrip().rstrip().upper())(' ngb '))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

p = lambda n:n*n*n
q = lambda x,y,z: (x+y+z)/3
r = lambda s:s.lstrip().rstrip().upper()
    
print(p(3))
print(q(10,20,30))
print(r(' jai hind'))