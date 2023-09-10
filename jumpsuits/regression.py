def linear_regression(dataframe, y_col, x_cols):
    """
    Performs linear regression on the given data.

    Parameters:
    - dataframe (pd.DataFrame): The data to perform regression on.
    - y_col (str): The dependent variable column.
    - x_cols (list): The independent variable(s) column(s).

    Returns:
    - regression_result (statsmodels.regression.linear_model.RegressionResultsWrapper): The regression results.
    """

    # Define the dependent and independent variables
    Y = dataframe[y_col]
    X = dataframe[x_cols]

    # Add a constant to the independent variable(s) for the intercept
    X = sm.add_constant(X)

    # Create a model
    model = sm.OLS(Y, X)

    # Fit the model
    regression_result = model.fit()

    # Print the summary of the regression
    print(regression_result.summary())

    return regression_result