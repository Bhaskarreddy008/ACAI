class Emp:
    def __init__(self, n, s): self.n, self.s = n, s
    def inc(self, p): self.s += self.s * p / 100
    def add_bonus(self, b): self.s += b
    def pr(self): print(f"emp: {self.n} salary: {self.s}")

e = Emp("RAJU", 5000)
e.inc(10)
e.add_bonus(500)
e.pr()
