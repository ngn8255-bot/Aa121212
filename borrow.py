from enroll_library import enroll_library
from _sex__ import _sex__
from _year__ import _year__
class library:
    def __init__(self,name):
        self.name = name
        self.account=[]
    def check_name(self):
        while True:
            if not self.name[0].isdigit() and self.name[1:].islower():
                self.account.append(self.name)
                break
            else:
                self.name=input('enter your name')


library.enroll_library=enroll_library
library._sex__=_sex__
library._year__=_year__

d=library('fang')
d.check_name()
d.enroll_library()
print('it is successful')






