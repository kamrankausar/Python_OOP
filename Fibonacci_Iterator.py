class Fib:
    """iterator that yields number in the Fibonacci sequence
    Note:
    __init__, __iter__ and __next__ are special method
    How to use
    from Fibonacci_Iterator import Fib
    for n in Fib(100):
        print(n, end = ' ' )
    """

    #Initilize the object i.e constructor
    def __init__(self, max):
        self.max = max


    #Iterator  nnnn

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

