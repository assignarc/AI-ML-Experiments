# 📈 W5: Linear Regression

> **Supervised Learning Module:** Regression modeling, assumptions, and evaluation

---

## 📋 Module Overview

**Focus:** Linear Regression from Fundamentals to Applications  
**Content:** 11 notebooks across 5 case studies  
**Difficulty:** Intermediate  
**Prerequisites:** W1-W4 (Python, Pandas, EDA, Stats)

---

## 📚 Case Studies

### 1. Anime Rating Prediction

**Directory:** `AnimeRating/`  
**Notebooks:** 2

**Objective:** Predict anime ratings based on features  
**Skills:** Multiple linear regression, feature selection

---

### 2. Auto MPG (Miles Per Gallon)

**Directory:** `AutoMPG/`  
**Notebooks:** 3

**Topics:**

- `LinearRegression_HandsOn.ipynb` - Basic implementation
- `LinearRegressionAssumptions_HandsOn.ipynb` - Validating assumptions

**Key Learnings:**

- Fuel efficiency prediction
- **Regression Assumptions Validation:**
  - Linearity
  - Homoscedasticity
  - Normality of residuals
  - Independence

---

### 3. Sales Forecasting

**Directory:** `Sales/`  
**Notebooks:** 2

**Objective:** Revenue prediction using multiple features  
**Applications:** Business forecasting, budgeting

---

### 4. Used Cars Pricing (Cars4u)

**Directory:** `UsedCars/`  
**Notebooks:** 2

**Objective:** Price prediction for used vehicles  
**Features:** Mileage, age, brand, condition, etc.  
**Business Impact:** Pricing strategy optimization

---

### 5. Practice Exercises

**Directory:** `Practice/`  
**Notebooks:** 2

**Focus:** Simple Linear Regression fundamentals  
**Content:** Step-by-step implementation from scratch

---

## 🎯 Techniques Covered

### Linear Regression Types

- **Simple Linear Regression:** Y = mx + b
- **Multiple Linear Regression:** Y = b₀ + b₁X₁ + b₂X₂ + ... + bₙXₙ

### Model Assumptions

1. **Linearity** - Linear relationship between X and Y
2. **Independence** - Observations are independent
3. **Homoscedasticity** - Constant variance of residuals
4. **Normality** - Residuals are normally distributed

### Feature Engineering

- Feature selection techniques
- Polynomial features
- Interaction terms
- Feature scaling/normalization

### Model Evaluation

- **R² Score** - Variance explained
- **Adjusted R²** - Penalized for number of features
- **RMSE** - Root Mean Squared Error
- **MAE** - Mean Absolute Error
- **MSE** - Mean Squared Error

### Diagnostics

- **Residual Plots** - Pattern detection
- **Q-Q Plots** - Normality testing
- **VIF** - Multicollinearity detection
- **Cook's Distance** - Influential points

---

## 💡 Skills Developed

✅ **Regression Modeling** - Build and evaluate linear models  
✅ **Assumption Testing** - Validate model prerequisites  
✅ **Feature Engineering** - Create and select features  
✅ **Model Diagnostics** - Identify and fix issues  
✅ **Interpretation** - Explain coefficients and predictions  
✅ **Business Application** - Translate models to insights

---

## 📁 Directory Structure

```
W5-LinearRegression/
├── AnimeRating/
│   └── Anime_Rating_Prediction_Notebook.ipynb
├── AutoMPG/
│   ├── LinearRegression_HandsOn.ipynb
│   ├── LinearRegressionAssumptions_HandsOn.ipynb
│   └── [data files]
├── Practice/
│   └── SLR_W1_PracticeExercise_Solution.ipynb
├── Sales/
│   └── Hands_on_Linear_Regression_Notebook.ipynb
├── UsedCars/
│   └── Cars4u_Notebook.ipynb
└── README.md (this file)
```

---

## 🚀 How to Use

### Installation

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels scipy
```

### Run Notebooks

```bash
cd W5-LinearRegression
jupyter notebook
```

**Recommended Learning Order:**

1. Practice exercises (Simple Linear Regression)
2. Auto MPG (Assumptions and validation)
3. Sales Forecasting
4. Cars4u (Practical application)
5. Anime Rating (Multiple features)

---

## 📊 Code Examples

### Simple Linear Regression

```python
from sklearn.linear_regression import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### Assumption Testing

```python
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# VIF for multicollinearity
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
```

---

## 🔗 Applied In Projects

- **P0:** Hotel pricing and cancellation prediction (regression for pricing)
- **Business forecasting:** Sales and revenue prediction
- **Pricing models:** Used car and product pricing

---

##🎓 Key Learnings

- **Start simple** - Begin with simple linear regression
- **Test assumptions** - They matter for reliable predictions
- **Feature engineering** is crucial for model performance
- **Residual analysis** reveals model weaknesses
- **Interpretation** is as important as accuracy

---

## 🔗 Links

- [Back to Main](../)
- [Previous: Text Analysis](../W4-AnalyzeTextData)
- [Next: Decision Trees](../W6-DecisionTree)

---

**Module:** W5 | **Notebooks:** 11 | **Case Studies:** 5 | **Type:** Regression
