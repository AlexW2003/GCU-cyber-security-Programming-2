import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
fileName = 'KDD_full.csv'
data = pd.read_csv(fileName)


dataMin = np.min(data['duration'])
dataMax = np.max(data['duration'])
print(dataMin)
print(dataMax)
data['duration'] = (data['duration'] - dataMin) / (dataMax-dataMin)

dataMin = np.min(data['duration'])
dataMax = np.max(data['duration'])
print(dataMin)
print(dataMax)


categoricalTCP = np.array(data['tcp'])
categoricalTCP = np.reshape(categoricalTCP,(-1,1))
encoder = OneHotEncoder(sparse=False, drop='if_binary')
numericalTCP =encoder.fit_transform(categoricalTCP)
data['tcp'] = numericalTCP


categoricalLabels = data['label']
categoricalLabels = np.array(categoricalLabels)
categoricalLabels = np.reshape(categoricalLabels,(-1,1))
# craete a label encoder
encoder = LabelEncoder()
numericalLabel = encoder.fit_transform(categoricalLabels)
# replace the encoded data in the dataset
data['label'] = numericalLabel
# saving the new dataset to disk
data.to_csv('lab_solution_data.csv')

# saving the new dataset to disk
data.to_csv('lab_solution_data.csv')
