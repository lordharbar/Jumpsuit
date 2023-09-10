import seaborn as sns
import matplotlib.pyplot as plt

def viz(dataframe, x_col, y_col, plot_type, title=None, xlabel=None, ylabel=None):
    """
    Visualizes the data using Seaborn.

    Parameters:
    - dataframe (pd.DataFrame): The data to visualize.
    - x_col (str): The column for the X-axis.
    - y_col (str): The column for the Y-axis, if applicable.
    - plot_type (str): The type of visualization ('scatter', 'line', 'bar', 'hist', 'box').
    - title (str, optional): The title of the plot.
    - xlabel (str, optional): The label for the X-axis.
    - ylabel (str, optional): The label for the Y-axis.

    Returns:
    - None. Displays the plot.
    """

    # Set the default style and context of the plot
    sns.set_style("dark")
    sns.set_context("notebook")

    # Determine plot type and visualize
    if plot_type == "scatter":
        sns.scatterplot(data=dataframe, x=x_col, y=y_col)
    elif plot_type == "line":
        sns.lineplot(data=dataframe, x=x_col, y=y_col)
    elif plot_type == "bar":
        sns.barplot(data=dataframe, x=x_col, y=y_col)
    elif plot_type == "hist":
        if not x_col:  # If x_col is not provided, y_col will be used
            sns.histplot(data=dataframe, x=y_col)
        else:
            sns.histplot(data=dataframe, x=x_col)
    elif plot_type == "box":
        sns.boxplot(data=dataframe, x=x_col, y=y_col)
    else:
        print(f"Unsupported plot type: {plot_type}")
        return

    # Apply customizations, if provided
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)

    # Remove the top and right spines
    sns.despine()

    # Display the plot
    plt.show()