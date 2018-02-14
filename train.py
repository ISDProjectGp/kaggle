import pandas as pd
import math
from passenger import Passenger
from label_probility import LabelProbability
from constant_type import survived
from constant_type import sex

df = pd.read_csv('train.csv')
df_t = pd.read_csv('test.csv')
passengers = []
validation_passengers = []
probability = []

for i in range(0, 800):
    passenger = Passenger()
    passenger.set_pclass(df['Pclass'][i])
    passenger.set_age(df['Age'][i])
    passenger.set_sex(df['Sex'][i])
    passenger.set_survived(df['Survived'][i])
    passengers.append(passenger)

for i in range(0, 418):
    passenger = Passenger()
    passenger.set_pclass(df_t['Pclass'][i])
    passenger.set_age(df_t['Age'][i])
    passenger.set_sex(df_t['Sex'][i])
    passenger.set_passengerid(df_t['PassengerId'][i])
    validation_passengers.append(passenger)



def test():
    print(passengers[1].survived)
    print(passengers[1].sex)
    print(passengers[1].age)
    print(passengers[1].pclass)


#  Summation(P(T|F))P(T)
def predict(array, passen, passengers):
    max = -1
    predict_label = None
    # for different labels
    for i in range(0, 2):
        givenProb = 1
        if not math.isnan(passen.age):
           givenProb *= array[i].age_count[int(passen.age) - 1] / array[i].lapace_counts
        givenProb *= array[i].pclass_count[passen.pclass - 1] / array[i].lapace_counts
        givenProb *= array[i].sex_count[passen.sex.value] / array[i].lapace_counts
        givenProb *= array[i].counts / len(passengers)
        if givenProb > max:
            max = givenProb
            predict_label = array[i].survived
    return predict_label


def train(array):
    # Given Probs
    labels_probability = []
    survived_label = LabelProbability()
    survived_label.survived = survived.survived

    not_survived_label = LabelProbability()
    not_survived_label.survived = survived.not_survived

    for i in range(0, len(array)):
        if array[i].survived == survived.survived:
            survived_label.counts += 1
            if not math.isnan(array[i].age):
                survived_label.age_count[int(array[i].age) - 1] += 1
            survived_label.sex_count[array[i].sex.value] += 1
            survived_label.pclass_count[array[i].pclass - 1] += 1
        elif array[i].survived == survived.not_survived:
            not_survived_label.counts += 1
            if not math.isnan(array[i].age):
                not_survived_label.age_count[int(array[i].age) - 1] += 1
            not_survived_label.sex_count[array[i].sex.value] += 1
            not_survived_label.pclass_count[array[i].pclass - 1] += 1
    survived_label.lapace_correction()
    not_survived_label.lapace_correction()
    labels_probability.append(survived_label)
    labels_probability.append(not_survived_label)

    return labels_probability


test_passenger = Passenger()
test_passenger.sex = sex.male
test_passenger.age = 25
test_passenger.pclass = 3

# Model training
trained_weight = train(passengers)
#print(predict(trained_weight, test_passenger, passengers))
# Kaggle Prediction

survive = []
id = []

for i in range(0, 418):
    validation_passengers[i].survived = predict(trained_weight, validation_passengers[i], passengers)
    if validation_passengers[i].survived == survived.survived:
        survive.append(1)
    elif validation_passengers[i].survived == survived.not_survived:
        survive.append(0)
    id.append(validation_passengers[i].passengerID)

raw_data = {"PassengerId": id,
        "Survived": survive
       }
df = pd.DataFrame(raw_data, columns = ['PassengerId', 'Survived'])
df.to_csv('submit.csv',index=False)



