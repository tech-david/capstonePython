# Setting paramater for length of testing months
# Using 66 months, corresponding to typical business cycle after WWII
from model.features.Preparation import complete_df


def train_test_split_business_cycle():
    test_size = 66
    df = complete_df()
    # Splitting features and target
    y = df['USREC']
    x = df.drop(columns=['USREC'],
                axis=1)
    x_train = x[:-test_size]
    x_test = x[-test_size:]
    y_train = y[:-test_size]
    y_test = y[-test_size:]
    return x_train, x_test, y_train, y_test
