import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

def handle_missing_values(data, strategy='mean'):
    """
    Handle missing values in the dataset.

    Parameters:
    - data (DataFrame): Input data.
    - strategy (str): Strategy for imputation ('mean', 'median', 'most_frequent').

    Returns:
    - DataFrame: Data with missing values handled.
    """
    imputer = SimpleImputer(strategy=strategy)
    data_imputed = imputer.fit_transform(data)
    return pd.DataFrame(data_imputed, columns=data.columns)

def scale_features(data):
    """
    Scale features of the dataset.

    Parameters:
    - data (DataFrame): Input data.

    Returns:
    - DataFrame: Scaled data.
    """
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    return pd.DataFrame(data_scaled, columns=data.columns)

def preprocess_data(file_path):
    """
    Preprocess data by handling missing values and scaling features.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - DataFrame: Preprocessed data.
    """
    # Load data
    data = load_data(file_path)

    # Handle missing values
    data = handle_missing_values(data)

    # Scale features
    data = scale_features(data)

    return data

# Example usage
if __name__ == "__main__":
    file_path = "data.csv"
    preprocessed_data = preprocess_data(file_path)
    print("Preprocessed data:")
    print(preprocessed_data.head())
