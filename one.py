import sys

class emp:
    raise_amount=0
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
    def apply_raise(self):
        self.pay= float(self.pay * self.raise_amount)
emp1=emp("prad","var",20)
emp2=emp("santu","var",20)
emp1.raise_amount=10
print (emp.apply_raise(emp1))
print (emp.apply_raise(emp2))
print((emp1.pay))
print((emp2.pay))
