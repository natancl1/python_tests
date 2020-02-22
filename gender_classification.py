from sklearn import tree, svm, neighbors, linear_model

clftree = tree.DecisionTreeClassifier() # Tree
clfsvm = svm.SVC() # Support Vector Machine (SVM)
clfnc = neighbors.NearestCentroid() # Nearest Centroid (NC)
clfsgd = linear_model.SGDClassifier(loss='hinge', penalty='l2', max_iter=1000) # Stochastic Gradient Descent (SGD)

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
    [190, 90, 47], [175, 64, 39],
    [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female','female', 'male', 'male']

clftree = clftree.fit(X, Y) # Tree
clfsvm = clfsvm.fit(X, Y) # SVM
clfnc = clfnc.fit(X, Y) # NC
clfsgd = clfsgd.fit(X, Y) # SGD

prediction_tree = clftree.predict([[190, 70, 43]]) # Tree
prediction_svm = clfsvm.predict([[190, 70, 43]]) # SVM
prediction_nc = clfnc.predict([[190, 70, 43]]) # NC
prediction_sgd = clfsgd.predict([[190, 70, 43]]) # SGD

print('Tree', prediction_tree) # Tree
print('SVM', prediction_svm) # SVM
print('NC', prediction_nc) # NC
print('SGD', prediction_sgd) # SGD
