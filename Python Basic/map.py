#map(function,iterable)

store=[("shirt",20.00),
       ("pants",25.00),
       ("jacket",50.00),
       ("socks",10.00)]

to_euro= lambda data :(data[0],data[1]*0.82)
store_euros=list(map(to_euro,store))
for i in store_euros:
    print(i)

