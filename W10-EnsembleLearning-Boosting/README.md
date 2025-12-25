# 🚀 W10: Ensemble Learning - Boosting

> **Advanced ML Module:** Sequential ensemble methods and boosting algorithms

---

## 📋 Module Overview

**Focus:** Boosting Algorithms (AdaBoost, GBM, XGBoost)  
**Content:** 4 notebooks across 2 case studies  
**Difficulty:** Advanced  
**Prerequisites:** W6 (Trees), W9 (Bagging)

---

## 📚 Case Studies

### 1. Credit Default Prediction

**Directory:** `CreditDefault/`  
**File:** `Ensemble_Boosting_Notebook.ipynb`  
**Objective:** Binary classification with boosting  
**Application:** Financial risk assessment

### 2. Wine Quality Prediction

**Directory:** `WineQuality/`  
**File:** `WineQuality_Prediction.ipynb`  
**Objective:** Multi-class quality rating prediction  
**Application:** Quality control and classification

---

## 🎯 Boosting Algorithms

### 1. AdaBoost (Adaptive Boosting)

- **Weighted Samples:** Misclassified samples get higher weights
- **Sequential Learning:** Each model corrects previous errors
- **Weak Learners:** Combines many weak models into strong model

### 2. Gradient Boosting

- **Loss Function Optimization:** Iteratively minimize loss
- **Gradients:** Each tree fits residual errors
- **Learning Rate:** Control contribution of each tree

### 3. XGBoost (Extreme Gradient Boosting)

- **Regularization:** L1/L2 to prevent overfitting
- **Parallel Processing:** Faster training
- **Tree Pruning:** Efficient tree building
- **Built-in CrossValidation**

---

## 💡 Key Concepts

**Bias-Variance Tradeoff:** Boosting reduces bias  
**Learning Rate:** Balance between speed and accuracy  
**n_estimators:** Number of boosting rounds  
**Sequential Training:** Cannot parallelize like bagging

---

## 📊 Performance Comparison

AdaBoost vs. Gradient Boosting vs. XGBoost:

- **Speed:** XGBoost > GBM > AdaBoost
- **Accuracy:** XGBoost ≥ GBM > AdaBoost
- **Overfitting Risk:** AdaBoost > GBM > XGBoost
- **Ease of Use:** AdaBoost > XGBoost > GBM

---

## 📁 Structure

```
W10-EnsembleLearning-Boosting/
├── CreditDefault/
│   └── Ensemble_Boosting_Notebook.ipynb
├── WineQuality/
│   └── WineQuality_Prediction.ipynb
└── README.md
```

---

## 🚀 Usage

```bash
pip install xgboost  # Additional package needed
cd W10-EnsembleLearning-Boosting
jupyter notebook
```

---

## 🔗 Applied In

**P3: EasyVisa** - Extensive use of AdaBoost, GBM, and XGBoost!

---

## 🔗 Links

- [Back to Main](../)
- [Previous: Ensemble Bagging](../W9-EnsembleLearning-Bagging)
- [Next: Model Tuning](../W11-EnsembleLearning-ModelTuning)

---

**Module:** W10 | **Type:** Ensemble | **Focus:** Boosting Algorithms
