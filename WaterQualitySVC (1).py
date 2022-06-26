'''
This program uses a Support Vector Classification model to classify water quality as potable (safe to drink) or 
non-potable (unfit to drink) based on 9 different characteristics. Test accuracy is ~70%, can be improved given more
time and data.
Data is taken from https://www.kaggle.com/datasets/adityakadiwal/water-potability
'''

# Pandas for data manipulation
import pandas

# sklearn for ML functions, such as the SVC model, train-test splitting, data scaling
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import os

#NOTE: Several libraries that were used but no longer needed were deleted to save space; matplotlib, seaborn, etc.


# Read and open the csv file
inDrive = "C:\\"
inPath = os.path.join(inDrive, "Users", "sumad", "OneDrive - San José Unified School District", "Documents", "WaterQualityData.csv")
dataframe = pandas.read_csv(inPath)

# Dataset contains ~3300 water samples


# Fill the missing values with median or mean based on the potable/non-potable distribution (40-60)
# Only ph, Sulfate, and Trihalomethanes columns have missing values
phCenter = dataframe["ph"].median()
sulfateCenter = dataframe["Sulfate"].mean()
trihalomethanesCenter = dataframe["Trihalomethanes"].median()
dataframe["ph"].fillna(value = phCenter, inplace = True)
dataframe["Sulfate"].fillna(value = sulfateCenter, inplace = True)
dataframe["Trihalomethanes"].fillna(value = trihalomethanesCenter, inplace = True)


# Seperate the features from the target column
feature_names = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']
x = dataframe[features]
y = dataframe['Potability']

# Scale the data meaningfully
feature_names = x.columns
ss = StandardScaler()
x[feature_names] = ss.fit_transform(x[feature_names])


# Split dataframe into train and test (25% allocated for test)
fTrain, fTest, tTrain, tTest = train_test_split(x, y, test_size = 0.25, random_state = 42)


# Initiate and fit the SVC 
model = SVC(kernel ='rbf',)
model.fit(fTrain, tTrain)

# Enter the values of the 9 attributes and the model will predict ie. ([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
model.predict([[]]) 



