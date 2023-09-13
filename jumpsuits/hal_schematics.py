import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

hal_config = {
    'logit': {
        'model': LogisticRegression(),
        'params': {'C': [0.001, 0.01, 0.1, 1, 10], 'penalty': ['l1', 'l2']}
    },
    'rf': {
        'model': RandomForestClassifier(),
        'params': {'n_estimators': [10, 50, 100, 200], 'max_depth': [None, 10, 20, 30], 'min_samples_split': [2, 5, 10]}
    },
    'svm': {
        'model': SVC(),
        'params': {'C': [0.001, 0.01, 0.1, 1, 10], 'kernel': ['linear', 'rbf']}
    },
    'xgb_c': {
        'model': xgb.XGBClassifier(),
        'params': {'learning_rate': [0.01, 0.05, 0.1], 'n_estimators': [100, 500, 1000], 'max_depth': [3, 5, 7], 'subsample': [0.7, 0.9, 1.0]}
    },
    'xgb_r': {
        'model': xgb.XGBRegressor(),
        'params': {'learning_rate': [0.01, 0.05, 0.1], 'n_estimators': [100, 500, 1000], 'max_depth': [3, 5, 7], 'subsample': [0.7, 0.9, 1.0]}
    }
}
