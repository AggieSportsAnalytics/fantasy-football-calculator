'''
Created on Feb 15, 2018

@author: asingh
'''

train_data = [[2, 12], [3, 62], [4, 114], [5, 69], [6, 149], [7, 100], [8, 85], [9, 222], [10, 143], [11, 134], [12, 51], [13, 74], [14, 95], [15, 145], [16, 52], [17, 141], [18, 182], [19, 328]]

#test_data = [[7, 10], [8, 8.5], [9, 22.2]]

closingPriceTrainData=328
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(train_data)
X_train = scaler.transform(train_data)


from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()
my_classifier.fit(train_data, train_target)

predictForMonths = [20]
print(train_data)

cost = closingPriceTrainData
for predictForMonth in predictForMonths:
    test_data = [[predictForMonth, cost]]
    predictions = my_classifier.predict(test_data)
    va = (predictions)
    #va = predictions

    cost = cost + va
    print(predictForMonth, va, cost)
