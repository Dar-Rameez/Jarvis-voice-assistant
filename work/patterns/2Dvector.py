class twoDvector:
    def __init__(self, i, j):
        self.i = i 
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

vector = twoDvector(3, 8)
vector.show()

vector2 = threeDvector(5, 9, 2)
vector2.show()