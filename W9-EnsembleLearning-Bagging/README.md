# 🎲 W9: Ensemble Learning - Bagging

> ** ML Module:** Bootstrap Aggregating and Random Forests

---

## 📋 Module Overview

**Focus:** Bagging Ensemble Methods 
**Content:** 4 notebooks across 2 case studies 
**Difficulty:** 
**Prerequisites:** W6 (Decision Trees)

---

## 📚 Case Studies

### 1. Diabetes Risk Prediction

**Directory:** `Diabetes/` 
**File:** `Case_Study_DiabetesRisk_Prediction.ipynb` 
**Objective:** Health risk assessment using ensemble methods 
**Application:** Medical diagnosis support

### 2. Loan Default Prediction

**Directory:** `LoanDefault/` 
**File:** `Ensemble_Bagging.ipynb` 
**Objective:** Credit risk modeling with bagging 
**Application:** Lending decisions

---

## 🎯 Key Concepts

### Bagging (Bootstrap Aggregating)

1. **Bootstrap Sampling:** Create multiple datasets with replacement
2. **Train Multiple Models:** One model per bootstrap sample
3. **Aggregate Predictions:** Voting (classification) or averaging (regression)

### Random Forest

- Extension of bagging for decision trees
- Additional randomness: random feature subset at each split
- **Out-of-Bag (OOB) Error:** Built-in validation

---

## 💡 Techniques

**Variance Reduction:** Combining models reduces overfitting 
**Feature Importance:** Aggregated across trees 
**OOB Estimation:** No need for separate validation set 
**Parallel Training:** Models train independently

---

## 📊 Comparison

Single Decision Tree vs. Bagging vs. Random Forest:

- **Accuracy:** RF > Bagging > Single Tree
- **Variance:** RF < Bagging < Single Tree
- **Interpretability:** Single Tree > Bagging > RF

---

## 📁 Structure

```
W9-EnsembleLearning-Bagging/
├── Diabetes/
│ └── Case_Study_DiabetesRisk_Prediction.ipynb
├── LoanDefault/
│ └── Ensemble_Bagging.ipynb
└── README.md
```

---

## 🚀 Usage

```bash
cd W9-EnsembleLearning-Bagging
jupyter notebook
```

---

## 🔗 Links

- [Back to Main](../)
- [Previous: Hierarchical Clustering](../W8-ClusteringHierarchical)
- [Next: Ensemble Boosting](../W10-EnsembleLearning-Boosting)

---

**Module:** W9 | **Type:** Ensemble | **Focus:** Bagging & Random Forest
