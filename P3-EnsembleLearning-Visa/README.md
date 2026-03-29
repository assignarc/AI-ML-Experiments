# Problem Statement
> Learning through experiments and data!

## What was the goal?
OFLC (Office of Foreign Labor Certification) needs to streamline visa approval decisions. Trying to:

## Why does this matter? (Business Context)
Placeholder: Why does this analysis matter for a business?

## Tech Stack
### Packages Needed For This Module:
- `VKPyKit`
- `imblearn`
- `matplotlib`
- `numpy`
- `pandas`
- `seaborn`
- `sklearn`
- `xgboost`

## Stuff I used (Libraries)
VKPyKit, imblearn, matplotlib, numpy, pandas, seaborn, sklearn, xgboost

## What did I notice?
The data contains the different attributes of employee and the employer. The detailed data dictionary is given below.

## What I Found (Insights)
- High Overfitting: The DecisionTree, Randomforest, and Bagging models show significant overfitting - near-perfect training scores (Accuracy $\approx$ 0.98–1.00) - sharp decline in performance on the Validation and Testing sets (Accuracy $\approx$ 0.65–0.72).
- Strong Generalization: GradientBoost and Adaboost most stable models - training scores are lower than the tree-based models - performance  consistent across all runs (Training, Validation, and Testing), looks like captured generalizable patterns rather than memorizing noise.

## What I Learned
- **Ensemble Methods:** Bagging, Boosting, Stacking in practice
- **Imbalanced Data:** Real-world strategies for handling skewed classes
- **Model Optimization:** Automated hyperparameter tuning (GridSearch is slow but worth it)
- **Feature Engineering:** Domain-specific transformations
- **Model Selection:** Trade-offs between different algorithms
- **Python Packaging:** Using custom ML libraries (VKPyKit)
- **MLOps Mindset:** Reproducible, scalable workflows

---

## How did it do? (Results)
Placeholder: Final model scores or summary.

## Wrapping up
Placeholder: Final thoughts.

