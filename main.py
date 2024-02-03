from analytics import data_preprocessing, feature_engineering, model_training
from visualization import trend_analysis, performance_metrics

def main():
    # Your main program logic here
    
    # Preprocess data
    file_path = "data.csv"
    preprocessed_data = data_preprocessing.preprocess_data(file_path)
    
    # Engineer features
    engineered_data = feature_engineering.engineer_features(preprocessed_data)
    
    # Train model
    target_variable = "target"
    trained_model = model_training.train_model(engineered_data, target_variable)
    
    # Visualize trends
    trend_analysis.visualize_trends()
    
    # Evaluate model performance
    X_test, y_test = engineered_data.drop(target_variable, axis=1), engineered_data[target_variable]
    y_pred = trained_model.predict(X_test)
    performance_metrics.visualize_performance_metrics(y_test, y_pred, labels=[0, 1])    

if __name__ == "__main__":
    main()
