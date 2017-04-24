with open('test', 'r') as f:
    a = []
    for i in f.readlines():
        a += i.split()
    print(len(a)
#    print(', '.join(a))
