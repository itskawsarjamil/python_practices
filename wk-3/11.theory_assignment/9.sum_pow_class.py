class sumpow:
    def __init__(self, X, n):
        self.X = X
        self.n = n

    def sum(self):
        return self.X+self.n

    def pow(self):
        c = 1
        for i in range(self.n):
            c = c*self.X
        return c

