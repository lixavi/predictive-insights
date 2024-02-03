import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression

def create_interaction_features(data):
    """
    Create interaction features based on existing features.

    Parameters:
    - data (DataFrame): Input data.

    Returns:
    - DataFrame: Data with interaction features.
    """
    interaction_data = data.copy()
    # Add interaction features (example)
    interaction_data['interaction_feature'] = interaction_data['feature1'] * interaction_data['feature2']
    return interaction_data

def select_best_features(data, target, k=5):
    """
    Select the best features using SelectKBest and f_regression.

    Parameters:
    - data (DataFrame): Input data.
    - target (str): Target variable name.
    - k (int): Number of features to select.

    Returns:
    - DataFrame: Data with selected best features.
    """
    X = data.drop(target, axis=1)
    y = data[target]
    selector = SelectKBest(score_func=f_regression, k=k)
    selected_features = selector.fit_transform(X, y)
    selected_indices = selector.get_support(indices=True)
    selected_feature_names = X.columns[selected_indices]
    return data[selected_feature_names]

def engineer_features(data):
    """
    Engineer features by creating interaction features and selecting the best features.

    Parameters:
    - data (DataFrame): Input data.

    Returns:
    - DataFrame: Data with engineered features.
    """
    # Create interaction features
    data = create_interaction_features(data)

    # Select best features
    data = select_best_features(data, target='target_variable', k=5)

    return data

# Example usage
if __name__ == "__main__":
    file_path = "data.csv"
    data = pd.read_csv(file_path)
    engineered_data = engineer_features(data)
    print("Engineered data:")
    print(engineered_data.head())
