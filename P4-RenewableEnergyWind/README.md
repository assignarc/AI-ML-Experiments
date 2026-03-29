# Problem Statement
> Learning through experiments and data!

## What was the goal?
“ReneWind” is a company working on improving the machinery/processes involved in the production of wind energy using machine learning and has collected data of generator failure of wind turbines using sensors. They have shared a ciphered version of the data, as the data collected through sensors is confidential (the type of data collected varies with companies). Data has 40 predictors, 20000 observations in the training set and 5000 in the test set.

## Why does this matter? (Business Context)
Renewable energy sources play an increasingly important role in the global energy mix, as the effort to reduce the environmental impact of energy production increases.

## Tech Stack
### Packages Needed For This Module:
- `VKPyKit`
- `copy`
- `imblearn`
- `matplotlib`
- `numpy`
- `pandas`
- `seaborn`
- `sklearn`
- `tensorflow`
- `xgboost`

## Stuff I used (Libraries)
VKPyKit, copy, imblearn, matplotlib, numpy, pandas, seaborn, sklearn, tensorflow, xgboost

## What did I notice?
The data provided is a transformed version of the original data which was collected using sensors.

## What I Found (Insights)
**Why AX9D-CW-SCALED model?**
1. Highest Recall: It captures roughly **94.6%** of all failures, the best performance in the set.
2. Robust Architecture: With 10 layers and 54k parameters, it has the depth to understand complex failure patterns without being overly massive.
3. Balanced F1-Score: While it prioritizes recall, it doesn't sacrifice too much precision (it isn't just "guessing" failure constantly), maintaining a high F1-score of 0.936.

## What I Learned
- **Data preprocessing** is crucial for neural network performance
- **Feature scaling** dramatically improves model convergence
- Deep learning excels at capturing **non-linear relationships**
- **Regularization techniques** (Dropout,Batch Norm) prevent overfitting
- Business context (cost analysis) guides **metric optimization**

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

