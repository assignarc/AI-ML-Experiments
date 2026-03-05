# 🌳 W6: Decision Trees

> **Classification Module:** Tree-based algorithms for classification and regression

---

## 📋 Module Overview

**Focus:** Decision Tree Algorithms and Applications 
**Content:** 6 notebooks across 3 case studies 
**Difficulty:** Intermediate 
**Prerequisites:** W1-W5 (Python, ML basics, Regression)

---

## 📚 Case Studies

### 1. Credit Card Approval

**Directory:** `CreditCard/` 
**Notebooks:** 2 
**File:** `CreeditCardApproval.ipynb`

**Objective:** Binary classification for credit decisions 
**Features:** Income, credit history, employment, etc. 
**Business Impact:** Risk assessment automation

**Key Concepts:**

- Binary classification
- Financial risk modeling
- Imbalanced data handling
- Feature importance in credit decisions

---

### 2. Loan Delinquency Prediction

**Directory:** `LoanDeliquency/` 
**Notebooks:** 2 
**File:** `Loan_Delinquent_Notebook.ipynb`

**Objective:** Predict loan default risk 
**Application:** Lending decisions, risk management 
**Skills:** Classification, probability calibration

**Learning Points:**

- Default risk factors
- Multi-class classification
- Cost-sensitive learning
- Business rule generation from trees

---

### 3. Machine Failure Prediction

**Directory:** `MachineFailure/` 
**Notebooks:** 2 
**File:** `Machine_Failure_Prediction_Notebook.ipynb`

**Objective:** Predictive maintenance 
**Domain:** Manufacturing, IoT 
**Outcome:** Reduce downtime, optimize maintenance

**Applications:**

- Time-series features
- Sensor data analysis
- Preventive vs. reactive maintenance
- Cost-benefit analysis

---

## 🎯 Core Concepts

### Decision Tree Algorithm

**How It Works:**

1. Select best feature to split on (using criterion)
2. Split data into subsets
3. Repeat recursively for each subset
4. Stop when criteria met (max_depth, min_samples, etc.)

### Splitting Criteria

**For Classification:**

- **Gini Impurity:** Measures class mixture
 - Lower is better (0 = pure node)
- **Entropy (Information Gain):** Measures disorder
 - Higher information gain = better split

**For Regression:**

- **MSE (Mean Squared Error):** Variance reduction

---

## 💡 Key Techniques

### Tree Parameters

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
 criterion='gini', # or 'entropy'
 max_depth=5, # Tree depth limit
 min_samples_split=20, # Min samples to split
 min_samples_leaf=10, # Min samples in leaf
 max_features='auto', # Features to consider
 random_state=42
)
```

### Preventing Overfitting

✅ **Pruning:** Limit tree depth 
✅ **Min samples:** Control node splits 
✅ **Cross-validation:** Validate generalization 
✅ **Ensemble methods:** Combine multiple trees (next modules)

### Feature Importance

```python
# Get feature importance
importances = model.feature_importances_
feature_importance_df = pd.DataFrame({
 'feature': X.columns,
 'importance': importances
}).sort_values('importance', ascending=False)
```

### Tree Visualization

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X.columns,
 class_names=['No', 'Yes'], filled=True)
plt.show()
```

---

## 📊 Skills Developed

✅ **Decision Tree Theory** - Understanding algorithms 
✅ **Classification** - Binary and multi-class problems 
✅ **Hyperparameter Tuning** - Optimizing tree parameters 
✅ **Feature Importance** - Identifying key variables 
✅ **Model Interpretation** - Visualizing decision paths 
✅ **Overfitting Control** - Pruning and regularization

---

## 📁 Directory Structure

```
W6 -DecisionTree/
├── CreditCard/
│ ├── CreeditCardApproval.ipynb
│ └── [data]
├── LoanDeliquency/
│ ├── Loan_Delinquent_Notebook.ipynb
│ └── [data]
├── MachineFailure/
│ ├── Machine_Failure_Prediction_Notebook.ipynb
│ └── [data]
└── README.md (this file)
```

---

## Running This
### Packages Needed For This Module:
- `VKPyKit`
- `matplotlib`
- `numpy`
- `pandas`
- `scipy`
- `seaborn`
- `sklearn`


### Installation

```bash
pip install pandas numpy matplotlib seaborn scikit-learn graphviz
```

### Run Notebooks

```bash
cd W6-DecisionTree
jupyter notebook
```

**Recommended Order:**

1. Credit Card Approval (binary classification basics)
2. Loan Delinquency (multi-class, cost-sensitivity)
3. Machine Failure (real-world application)

---

## 🎓 Advantages & Limitations

### Advantages ✅

- **Interpretable:** Easy to understand and explain
- **Non-parametric:** No assumptions about data distribution
- **Handle mixed data:** Numerical and categorical
- **Feature importance:** Built-in feature selection
- **Non-linear:** Captures complex patterns

### Limitations ⚠️

- **Overfitting:** Can create overly complex trees
- **Instability:** Small data changes can alter tree
- **Greedy:** Local optimization at each split
- **Bias:** Towards features with more levels

**Solution:** Ensemble methods (W9-W11)

---

## 🔗 Applied In Projects

- **P2: Personal Loan Campaign** - Decision Tree for customer targeting (direct application!)
- **Credit risk models** - Financial decision making
- **Classification tasks** - Various business problems

---

## 🔜 Foundation For

- **W9:** Bagging and Random Forests
- **W10:** Boosting algorithms (AdaBoost, GBM, XGBoost)
- **W11:** Ensemble optimization

---

## 🔗 Links

- [Back to Main](../)
- [Previous: Linear Regression](../W5-LinearRegression)
- [Next: K-Means Clustering](../W7-ClusteringKMeans)

---

**Module:** W6 | **Notebooks:** 6 | **Case Studies:** 3 | **Type:** Classification
