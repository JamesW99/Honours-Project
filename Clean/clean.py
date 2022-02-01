import pandas as pd
import numpy as np

# data = pd.read_csv('../geometry.csv')
data = pd.read_csv('~/data.csv',
                   # nrows=1000,
                   usecols={'Reach', 'Stack', 'BB Drop', 'BB Height', 'Chainstay', 'Fork Length (A2C)', 'Front Centre',
                            'Head Angle', 'Head Tube', 'Seat Angle', 'Seat Tube C-T', 'Standover',
                            'Top Tube (effective)', 'Wheelbase'})

data.replace('\s+', '', regex=True, inplace=True)

# delete all non numeric rows.
for i in data:
    data = data.drop(data[data[i].str.contains("\\D", regex=True) == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('-') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('–') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('m') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains(',') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains(' ̊') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('−') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('"') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('(') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('+') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains("*") == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('+') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains('/') == True].index, axis=0)
    # data = data.drop(data[data[i].str.contains("\") == True].index)


def isNumeric(feature):
    counter = 0
    # print('Non numeric of '+ feature + ':')
    for i in range(data.shape[0]):
        try:
            float(data[feature][i])
        except:
            if (pd.isna(data[feature][i])):
                # print(i+1,'is null')
                pass
            else:
                counter += 1
                print(i + 2, 'is:', data[feature][i])
                pass

    print(counter, feature, 'is non numeric.')


data.reset_index(inplace=True)
for j in data:
    # print(j)
    isNumeric(j)

print(data)



data.to_csv('~/numeric.csv')