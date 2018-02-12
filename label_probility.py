
class LabelProbability:



    def __init__(self):
        # Variables
        self.pclass_count = [0, 0, 0]  # class 1 / class 2 / class 3
        self.age_count = []  # AGE
        # fare = 0  # FARE
        self.sex_count = [0, 0]  # SEX MALE / FEMALE
        self.survived = 0  # Survived
        self.counts = 0  # Counts
        self.lapace_counts = 0
        for i in range(0,120):
            self.age_count.append(0)

    def plus_one(self):
        for i in range(0,120):
            self.age_count[i] +=1
            self.lapace_counts +=1
        for j in range(0,3):
            self.pclass_count[j] +=1
            self.lapace_counts += 1
        for k in range(0,2):
            self.sex_count[k] += 1
            self.lapace_counts += 1


    def lapace_correction(self):
        self.lapace_counts = self.counts
        plus = False
        for i in range(0, 120):
            if self.age_count[i] == 0 : plus = True
        for j in range(0, 3):
            if self.pclass_count[j] == 0 : plus = True
        for k in range(0, 2):
            if self.sex_count[k] == 0 : plus = True
        if plus:
            self.plus_one()
