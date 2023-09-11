from sklearn.model_selection import train_test_split

def suit_split(X, y, test_size=0.2):
    """
    Splits the dataset into training and testing sets.

    Parameters:
    - X: Features (pandas DataFrame or Series)
    - y: Target variable (pandas DataFrame or Series)
    - test_size: Proportion of the dataset to include in the test split (float)

    Returns:
    - X_train, X_test, y_train, y_test: Split datasets
    """
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    return X_train, X_test, y_train, y_test