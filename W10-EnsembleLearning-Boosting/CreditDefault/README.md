# Ensemble Hands On - Boosting
> Learning through experiments and data!

## What was the goal?
Placeholder: Describe the goal here.

## Why does this matter? (Business Context)
Placeholder: Why does this analysis matter for a business?

## Tech Stack
Matplotlib, NumPy, Pandas, Scikit-learn, Seaborn, Vkpykit, Xgboost

## Stuff I used (Libraries)
VKPyKit, matplotlib, numpy, pandas, seaborn, sklearn, xgboost

## What did I notice?
Placeholder: What interesting things popped up in the data?

## What I Found (Insights)
- The model is overfitting the train data as train accuracy is much higher than the test accuracy.
- The model has low test recall. This implies that the model is not good at identifying defaulters.
- Amount is the most important feature as per the tuned AdaBoost model.
- Most of the hyperparameters available are same as random forest classifier.
- init: An estimator object that is used to compute the initial predictions. If ‘zero’, the initial raw predictions are set to zero. By default, a DummyEstimator predicting the classes priors is used.
- There is no class_weights parameter in gradient boosting.
**Let's try using AdaBoost classifier as the estimator for initial predictions**
**As compared to the model with default parameters:**

## What I Learned
Placeholder: What was the biggest takeaway?

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

