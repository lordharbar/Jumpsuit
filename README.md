# 🚀 Jumpsuits 👨‍🚀

Jumpsuits is your trusty companion for all your data explorations. Just as an astronaut relies on their jumpsuit, data explorers and scientists can rely on this package for quick data visualizations, linear regression, and more (I promise my left foot I will continue to update this)!

## Features

- **Easy Data Visualization**: With a single function, visualize your data using various plot types including scatterplots, line graphs, and more.
- **Linear Regression**: Perform simple and multivariate linear regressions seamlessly.

## Installation

To install the Jumpsuits package:

```
pip install -e path/to/jumpsuits
```
## Usage
### Data Visualization

First, ensure you have your data in a pandas DataFrame. Then use the viz function:
```
from jumpsuits import vizz
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Using the viz function for visualization
vizz.hud(df, 'A', 'B', 'scatter')

```
### Linear Regression

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

### Train, Test, Split

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

X_train, X_test, y_train, y_test = suit_split(X, y, test_size=0.3)
```

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome, but you totally don't have to, but you can, it's up to you.

## Licensing
The code in this project is licensed under MIT license.