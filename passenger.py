from constant_type import survived
from constant_type import sex

class Passenger:
    # Constant
    FEMALE = "female"
    MALE = "male"

    def __init__(self):
        # Variables
        self.pclass = 0  # PASSENGER CLASS
        self.age = 0  # AGE
        # fare = 0  # FARE
        self.sex = None  # SEX
        self.survived = 0  # Survived
        self.passengerID = 0

    # Getter and Setter
    def set_pclass(self, pclass):
        self.pclass = pclass

    def set_survived(self, survive):
        if survive == 0:
            self.survived = survived.not_survived
        elif survive == 1:
            self.survived = survived.survived

    def set_passengerid(self,id):
        self.passengerID = id

    def set_sex(self, sexString):
        if sexString == self.FEMALE:
            self.sex = sex.female
        elif sexString == self.MALE:
            self.sex = sex.male

    ##def set_fare(self, fare):
    ##self.fare = fare

    def set_age(self, age):
        self.age = age
