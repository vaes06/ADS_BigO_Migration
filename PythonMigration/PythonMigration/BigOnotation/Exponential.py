
n = 40
class Exp:
    def __init__(self, a):
        self.a = a

    def fibcalc(self, a):
        if a < 0:
            Exception("n can not be less than zero")
        if a <= 2:
            return 1

        fib = Exp(a-1).fibcalc(a-1) + Exp(a-2).fibcalc(a-2)
        return fib


for i in range(1, (n+1)):
    fibonacci = Exp(i).fibcalc(i)
    print("Fibbonacci", i, " = ", fibonacci)
