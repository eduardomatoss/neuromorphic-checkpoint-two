from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression


def predict_model(df):
    y_prediction = df[["moisture"]]
    x_data = df.drop("moisture", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        x_data, y_prediction, test_size=0.2, random_state=42
    )

    lm = LinearRegression()
    lm.fit(X_train, y_train)
    y_pred = lm.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    return X_test, y_test, y_pred, r2, mse, mae
