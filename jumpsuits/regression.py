# regression baybay

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

# regression formula
def get_linear_formula(regression_result, y_col, x_cols):
    """
    Generates the linear formula from the regression result.

    Parameters:
    - regression_result (statsmodels.regression.linear_model.RegressionResultsWrapper): The regression results.
    - y_col (str): The dependent variable column name.
    - x_cols (list): The independent variable(s) column(s) names.

    Returns:
    - formula (str): The linear formula.
    """

    # Extracting coefficients and the intercept
    coefficients = regression_result.params
    formula_terms = [f"{y_col} = {coefficients[0]:.4f} (Intercept)"]

    for idx, col in enumerate(x_cols, 1):
        formula_terms.append(f"{coefficients[idx]:+.4f}*{col}")

    formula = " + ".join(formula_terms)
    return formula
