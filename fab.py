
def fab(max): 
    L = []
    n, a, b = 0, 0, 1 
    while n < max: 
        L.append(b) 
        a, b = b, a + b 
        n = n + 1
    return L


class Fab(object): 
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 

    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()
