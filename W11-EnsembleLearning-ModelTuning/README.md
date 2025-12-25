# ⚙️ W11: Model Tuning & Optimization

> **Advanced ML Module:** Hyperparameter optimization and advanced model validation

---

## 📋 Module Overview

**Focus:** Model optimization, cross-validation, imbalanced data  
**Content:** 7 notebooks across 3 case studies  
**Difficulty:** Advanced  
**Prerequisites:** W6-W10 (All ML modules)

---

## 📚 Case Studies

### 1. Diabetes Dataset

**Directory:** `Diabetes/`  
**File:** `K_fold_cross_validation_Notebook.ipynb`  
**Focus:** K-fold cross-validation techniques  
**Skills:** Robust model evaluation

### 2. Job Market Data

**Directory:** `JobData/`  
**File:** `MLS3_ETMT_session_notebook_updated.ipynb`  
**Focus:** Employment prediction with tuned models  
**Skills:** Hyperparameter optimization

### 3. Loan Dataset

**Directory:** `Loans/`  
**Files:**

- `Hyperparameter_tuning_Notebook.ipynb`
- `Oversampling_and_undersampling_Notebook.ipynb`

**Focus:** Class imbalance handling + hyperparameter tuning  
**Skills:** SMOTE, undersampling, GridSearch

---

## 🎯 Techniques Covered

### Cross-Validation

- **K-Fold Cross-Validation:** Robust evaluation
- **Stratified K-Fold:** Maintain class distribution
- **Nested Cross-Validation:** Unbiased hyperparameter selection

### Hyperparameter Tuning

- **GridSearchCV:** Exhaustive search over parameter grid
- **RandomizedSearchCV:** Random sampling for efficiency
- **Parameter distributions:** Continuous and discrete

### Class Imbalance

- **SMOTE:** Synthetic Minority Over-sampling Technique
- **Random Undersampling:** Balance majority class
- **Combined Approaches:** Over + undersampling
- **Cost-Sensitive Learning:** Weighted classes

### Pipeline Creation

- **sklearn Pipeline:** Reproducible workflows
- **Parameter naming:** For grid search in pipelines
- **Cross-validation with pipelines:** Prevent data leakage

---

## 💡 Skills Developed

✅ **K-Fold CV:** Robust model validation  
✅ **GridSearch:** Systematic hyperparameter tuning  
✅ **RandomizedSearch:** Efficient parameter sampling  
✅ **SMOTE:** Handle imbalanced datasets  
✅ **Pipeline:** Reproducible ML workflows  
✅ **Nested CV:** Unbiased evaluation

---

## 📊 Code Examples

### GridSearchCV

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15],
    'learning_rate': [0.01, 0.1, 0.3]
}

grid_search = GridSearchCV(
    estimator=XGBClassifier(),
    param_grid=param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
```

### SMOTE

```python
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
```

### Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
```

---

## 📁 Structure

```
W11-EnsembleLearning-ModelTuning/
├── Diabetes/
│   └── K_fold_cross_validation_Notebook.ipynb
├── JobData/
│   └── MLS3_ETMT_session_notebook_updated.ipynb
├── Loans/
│   ├── Hyperparameter_tuning_Notebook.ipynb
│   └── Oversampling_and_undersampling_Notebook.ipynb
└── README.md
```

---

## 🚀 Usage

```bash
pip install imbalanced-learn  # For SMOTE
cd W11-EnsembleLearning-ModelTuning
jupyter notebook
```

**Recommended Order:**

1. K-fold cross-validation (Diabetes)
2. Hyperparameter tuning (Loans)
3. SMOTE and sampling (Loans)
4. Complete workflow (JobData)

---

## 🔗 Applied In Projects

**P3: EasyVisa** - Extensive application of ALL W11 techniques:

- GridSearchCV and RandomizedSearchCV for tuning
- SMOTE for oversampling
- Random undersampling
- Complete comparison of techniques

---

## 🎓 Best Practices

✅ **Always use cross-validation** for model evaluation  
✅ **Grid search with CV** to avoid overfitting to validation set  
✅ **Try SMOTE** for imbalanced classification  
✅ **Pipeline everything** for reproducibility  
✅ **Monitor multiple metrics** (accuracy, precision, recall, F1)  
✅ **Consider computational cost** of exhaustive grid search

---

## 🔗 Links

- [Back to Main](../)
- [Previous: Ensemble Boosting](../W10-EnsembleLearning-Boosting)

---

**Module:** W11 | **Notebooks:** 7 | **Type:** Optimization | **Advanced Techniques**
