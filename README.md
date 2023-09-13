# 🚀 Jumpsuit 👨‍🚀

Jumpsuit is your trusty companion for all your data explorations. Just as an astronaut relies on their jumpsuit, data explorers and scientists can rely on this package for quick data visualizations, linear regression, and more (I promise my left foot I will continue to update this)!

## Features

- **Easy Data Visualization**: With a single function, visualize your data using various plot types including scatterplots, line graphs, and more.
- **Linear Regression**: Perform simple and multivariate linear regressions seamlessly, and produces a simple regression formula.
- **Train Test Split**: Train test split your pandas data frame in one easy to use function.

## Installation

To install the Jumpsuits package:

```
pip install -e path/to/jumpsuit
```
## Usage
### Jumpsuits Library: vizz module

Use the vizz module to easily create seaborn based visualizationa from your pandas DataFrame

First, ensure you have your data in a pandas DataFrame. Then use the viz function:
```
from jumpsuits import vizz
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Using the viz function for visualization
vizz.hud(df, 'A', 'B', 'scatter')

```
### Jumpsuits Library: suit_fit module

Use the suit_fit and get_tailor functions for regression analysis:

```
from jumpsuits import regression
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'Y': [1, 2, 3, 4],
    'X1': [5, 6, 7, 8],
    'X2': [9, 10, 11, 12]
})

# Performing linear regression
result = regression.suit_fit(df, 'Y', ['X1', 'X2'])

# Getting the linear formula
print(regression.get_tailor(result, 'Y', ['X1', 'X2']))

```

### Jumpsuits Library: tts module

Use the suit_split function for train, test, split a Pandas DataFrame

```
from jumpsuits import tts
import pandas as pd

# Sample DataFrame
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 6, 7, 8, 9],
    'target': [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df[['feature1', 'feature2']]
y = df['target']

X_train, X_test, y_train, y_test = tts.suit_split(X, y, test_size=0.3)
```
## Jumpsuits Library: HAL Module

The HAL (Heuristic Algorithmic Learning) module of the Jumpsuits library is a versatile tool designed to train machine learning models seamlessly. At the heart of HAL is the train_hal function, which allows the user to quickly deploy and optionally tune several types of machine learning models.

Dependencies:
* pandas
* sklearn
* xgboost

### Files
hal.py: Contains the core functions, including train_hal.
hal_schematics.py: Houses configurations for various models, including hyperparameters to be tuned.

### Functions
#### Usage: train_hal
```
def train_hal(data, X_cols, y_col, model_type='xgb_c', tune_hyperparameters=True):
```

### Parameters:

* data (pandas.DataFrame): Input DataFrame containing the data.
* X_cols (List[str]): List of column names to be used as features.
* y_col (str): The column name of the target variable.
* model_type (str, default='logistic'): Specifies the type of model to be trained. Options include:
    * 'logistic': Logistic Regression
    * 'random_forest': Random Forest Classifier
    * 'svm': Support Vector Machine
    * 'xgb_classifier': XGBoost Classifier
    * 'xgb_regressor': XGBoost Regressor
    * tune_hyperparameters (bool, default=False): If set to True, the function will search for optimal hyperparameters using cross-validation. The set of hyperparameters to be searched is defined in model_configurations.py.

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome, but you totally don't have to, but you can, it's up to you.

## Licensing
The code in this project is licensed under MIT license.