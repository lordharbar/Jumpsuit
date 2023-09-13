from tts import suit_split
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
from hal_schematics import hal_config
from sklearn.model_selection import train_test_split, GridSearchCV

# Your train_hal function and other code here...


def train_hal(data, X_cols, y_col, model_type='logistic', tune_hyperparameters=False):
    """
    Train a machine learning model with optional hyperparameter tuning using HAL (Heuristically programmed ALgorithmic computer).

    Parameters:
    - data: Input DataFrame
    - X_cols: List of feature column names
    - y_col: Target column name
    - model_type: Type of model to train ('logistic', 'random_forest', 'svm')
    - tune_hyperparameters: Boolean to decide if hyperparameters should be optimized

    Returns:
    - Trained model (optionally hyperparameter-optimized)
    """
    
    # Split data
    X = data[X_cols]
    y = data[y_col]
    X_train, X_test, y_train, y_test = tts.suit_split(X, y, test_size=0.3)
    
    # Model configurations
    model_config = {
        'logistic': {
            'model': LogisticRegression(),
            'params': {
                'C': [0.001, 0.01, 0.1, 1, 10],
                'penalty': ['l1', 'l2']
            }
        },
        'random_forest': {
            'model': RandomForestClassifier(),
            'params': {
                'n_estimators': [10, 50, 100, 200],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10]
            }
        },
        'svm': {
            'model': SVC(),
            'params': {
                'C': [0.001, 0.01, 0.1, 1, 10],
                'kernel': ['linear', 'rbf']
            }
        }
    }
    
    # Ensure valid model_type
    if model_type not in model_config:
        raise ValueError("Unsupported model type!")

    # Get model and parameters
    model = model_config[model_type]['model']
    params = model_config[model_type]['params']
    
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

# Example usage:
# data = pd.read_csv('your_data.csv')
# trained_model = train_hal(data, ['feature1', 'feature2'], 'target', model_type='random_forest', tune_hyperparameters=True)
