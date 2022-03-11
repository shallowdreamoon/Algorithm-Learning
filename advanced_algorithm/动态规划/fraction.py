"""
最大公约数的应用：
实现分数计算
"""
class Fraction:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        x=self.gcd_no_recursion(a,b)
        self.a/=x
        self.b/=x

    def zgs(self,a,b):
        x=self.gcd_no_recursion(a,b)
        return a*b/x

    @staticmethod
    def gcd_no_recursion(a, b):
        while b > 0:
            t = a % b
            a = b
            b = t
        return a

    def __add__(self, other):
        a=self.a
        b=self.b
        c=other.a
        d=other.b
        deno=self.zgs(b,d)
        mol=a*(deno/b)+c*(deno/d)
        return Fraction(mol,deno)

    def __str__(self):
        return "%d/%d" % (self.a,self.b)

f=Fraction(30,15)
print(f)

a=Fraction(1,2)
b=Fraction(1,3)
print(a+b)