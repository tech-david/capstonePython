from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR

from model.dataset.TrainTestData import train_test_split_business_cycle

x_train, y_train, x_test, y_test = train_test_split_business_cycle()

models = [('LR', LinearRegression()), ('NN', MLPRegressor(solver='lbfgs')), ('KNN', KNeighborsRegressor()),
          ('RF', RandomForestRegressor(n_estimators=10)), ('SVR', SVR(gamma='auto'))]

results = []
names = []
for name, model in models:
    tscv = TimeSeriesSplit(n_splits=10)
    cv_results = cross_val_score(model,
                                 x_train,
                                 y_train,
                                 cv=tscv,
                                 scoring='r2')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name,
                           cv_results.mean(),
                           cv_results.std()))