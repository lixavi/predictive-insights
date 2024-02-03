from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

def plot_confusion_matrix(y_true, y_pred, labels):
    """
    Plot confusion matrix.

    Parameters:
    - y_true (array-like): True labels.
    - y_pred (array-like): Predicted labels.
    - labels (list): List of class labels.

    Returns:
    - None
    """
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()

def evaluate_classification(y_true, y_pred):
    """
    Evaluate classification performance.

    Parameters:
    - y_true (array-like): True labels.
    - y_pred (array-like): Predicted labels.

    Returns:
    - dict: Dictionary containing classification report metrics.
    """
    classification_metrics = classification_report(y_true, y_pred, output_dict=True)
    return classification_metrics

def visualize_classification_report(classification_metrics):
    """
    Visualize classification report metrics.

    Parameters:
    - classification_metrics (dict): Dictionary containing classification report metrics.

    Returns:
    - None
    """
    df_classification = pd.DataFrame(classification_metrics).transpose()
    df_classification.drop(columns=['support'], inplace=True)
    print("Classification Report:")
    print(df_classification)

def calculate_accuracy(y_true, y_pred):
    """
    Calculate accuracy score.

    Parameters:
    - y_true (array-like): True labels.
    - y_pred (array-like): Predicted labels.

    Returns:
    - float: Accuracy score.
    """
    return accuracy_score(y_true, y_pred)

def visualize_performance_metrics(y_true, y_pred, labels):
    """
    Visualize performance metrics for classification.

    Parameters:
    - y_true (array-like): True labels.
    - y_pred (array-like): Predicted labels.
    - labels (list): List of class labels.

    Returns:
    - None
    """
    # Plot confusion matrix
    plot_confusion_matrix(y_true, y_pred, labels)

    # Evaluate classification
    classification_metrics = evaluate_classification(y_true, y_pred)
    visualize_classification_report(classification_metrics)

    # Calculate accuracy
    accuracy = calculate_accuracy(y_true, y_pred)
    print("Accuracy:", accuracy)

# Example usage
if __name__ == "__main__":
    y_true = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
    y_pred = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
    labels = [0, 1]
    visualize_performance_metrics(y_true, y_pred, labels)
