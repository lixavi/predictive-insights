from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def split_data(data, target_variable, test_size=0.2):
    """
    Split the data into training and testing sets.

    Parameters:
    - data (DataFrame): Input data.
    - target_variable (str): Name of the target variable.
    - test_size (float): Size of the testing set.

    Returns:
    - tuple: Tuple containing training and testing data.
    """
    X = data.drop(target_variable, axis=1)
    y = data[target_variable]
    return train_test_split(X, y, test_size=test_size, random_state=42)

def train_random_forest_regressor(X_train, y_train):
    """
    Train a Random Forest Regressor model.

    Parameters:
    - X_train (DataFrame): Features of the training set.
    - y_train (Series): Target variable of the training set.

    Returns:
    - RandomForestRegressor: Trained Random Forest Regressor model.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.

    Parameters:
    - model: Trained model.
    - X_test (DataFrame): Features of the testing set.
    - y_test (Series): Target variable of the testing set.

    Returns:
    - float: Root Mean Squared Error (RMSE) of the model.
    """
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    return rmse

def train_model(data, target_variable):
    """
    Train a predictive model using Random Forest Regressor.

    Parameters:
    - data (DataFrame): Input data.
    - target_variable (str): Name of the target variable.

    Returns:
    - RandomForestRegressor: Trained Random Forest Regressor model.
    """
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(data, target_variable)

    # Train Random Forest Regressor model
    model = train_random_forest_regressor(X_train, y_train)

    # Evaluate the model
    rmse = evaluate_model(model, X_test, y_test)
    print("Root Mean Squared Error:", rmse)

    return model

# Example usage
if __name__ == "__main__":
    file_path = "data.csv"
    target_variable = "target"
    data = pd.read_csv(file_path)
    trained_model = train_model(data, target_variable)
