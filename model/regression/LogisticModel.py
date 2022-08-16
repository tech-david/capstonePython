from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score
from model.dataset.TrainTestData import train_test_split_business_cycle

x_train, x_test, y_train, y_test = train_test_split_business_cycle()
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model().predict(x_test)


def model_accuracy():
    accuracy = model.score(x_test, y_test)
    return accuracy


def confusion_matrix_report():
    report = confusion_matrix(y_test, y_pred)
    return report


def model_classification():
    report = classification_report(y_test, y_pred)
    return report


def model_roc_auc_score():
    score = roc_auc_score(y_test,
                          model.predict(x_test))
    return score


def model_roc_curve():
    fpr, tpr, thresholds = roc_curve(y_test,
                                     model.predict_proba(x_test)[:, 1])
    return fpr, tpr, thresholds
