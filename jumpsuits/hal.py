from tts import suit_split
from hal_schematics import hal_config
from sklearn.model_selection import GridSearchCV

# train_hal function

def train_hal(data, X_cols, y_col, model_type='logistic', tune_hyperparameters=False):
    """
    Train a machine learning model with optional hyperparameter tuning using HAL.

    Parameters:
    - data: Input DataFrame
    - X_cols: List of feature column names
    - y_col: Target column name
    - model_type: Type of model to train [xgb_r, xgb_c, logit, rf, svm,]
    - tune_hyperparameters: Boolean to decide if hyperparameters should be optimized

    Returns:
    - Trained model (optionally hyperparameter-optimized)
    """
    
    # Split data
    X = data[X_cols]
    y = data[y_col]
    X_train, X_test, y_train, y_test = tts.suit_split(X, y, test_size=0.3)
    
    # Ensure valid model_type
    if model_type not in hal_config:
        raise ValueError("Unsupported model type!")

    # Get model and parameters from the imported hal_config
    model = hal_config[model_type]['model']
    params = hal_config[model_type]['params']
    
    # Tune hyperparameters if required
    if tune_hyperparameters:
        grid_search = GridSearchCV(model, params, cv=5)
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        print(f"Best parameters: {grid_search.best_params_}")
        return best_model

    # Train model without tuning
    model.fit(X_train, y_train)
    return model


