from _year__ import _year__
from _sex__ import _sex__
from enroll_library import enroll_library


class Library:
    def __init__(self):
        self.name = None
        self.sex = None
        self.year = None

    # three ways
    _year__ = _year__
    _sex__ = _sex__
    enroll_library = enroll_library

    # we complete registration
    def complete_registration(self):
        if self.name and self.sex and self.year:
            print(f'registration completed!')
            print(f'name: {self.name}, sex: {self.sex}, year: {self.year}')
        else:
            print('incomplete information, registration failed')


#running window
if __name__ == '__main__':
    lib = Library()
    lib.enroll_library()  # check name
    lib._sex__()  # check sex
    lib.complete_registration()  # check enrollment result






