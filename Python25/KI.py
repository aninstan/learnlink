from sklearn.neighbors import KNeighborsClassifier

X = [[190],[150],[162],[134],[156],[168],[131],[166],[187], [178], [180]]
y = ['høy', 'lav', 'lav','lav', 'lav', 'lav', 'lav', 'lav','høy','høy','høy']

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X, y)

ny_hoyde = [[181]]
pred = knn.predict(ny_hoyde)

print(pred)