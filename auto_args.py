def func(*args):
    for i in args:
        print(i)


func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'problem')

def func2(*args, **kwargs):
    print(kwargs)
    for i in kwargs.items():
        print(i)

func2(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)

