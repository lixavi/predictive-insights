import pandas as pd
import matplotlib.pyplot as plt

def plot_trends(data, x_variable, y_variable):
    """
    Plot trends between two variables.

    Parameters:
    - data (DataFrame): Input data.
    - x_variable (str): Name of the independent variable (X-axis).
    - y_variable (str): Name of the dependent variable (Y-axis).

    Returns:
    - None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data[x_variable], data[y_variable], marker='o', linestyle='-')
    plt.title(f"Trend Analysis: {y_variable} vs {x_variable}")
    plt.xlabel(x_variable)
    plt.ylabel(y_variable)
    plt.grid(True)
    plt.show()

def visualize_trends():
    """
    Visualize trends between two variables.

    Parameters:
    - None

    Returns:
    - None
    """
    # Load data (example)
    data = pd.DataFrame({
        'year': [2016, 2017, 2018, 2019, 2020],
        'revenue': [100000, 120000, 150000, 180000, 200000]
    })

    # Plot trends
    plot_trends(data, x_variable='year', y_variable='revenue')

# Example usage
if __name__ == "__main__":
    visualize_trends()
