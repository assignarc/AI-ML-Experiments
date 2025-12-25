# 💳 Personal Loan Campaign - AllLife Bank

> **Classification Project:** Predicting customer propensity to accept personal loan offers for targeted marketing

---

## 📋 Project Overview

**Domain:** Banking & Financial Services  
**Project Type:** Binary Classification  
**Difficulty Level:** Intermediate

### Business Problem

AllLife Bank wants to increase the number of customers accepting personal loans. Currently, only 9.6% of customers accept loan offers. The bank needs to:

- Identify characteristics of customers likely to accept loans
- Build a predictive model for targeted campaigns
- Optimize marketing spend by focusing on high-propensity customers
- Understand key drivers of loan acceptance

---

## 📊 Dataset

**Source:** AllLife Bank customer data  
**Records:** 5,000 customer records  
**Features:** 14 variables  
**Target Variable:** `Personal_Loan` (Binary: 0 = Not Accepted, 1 = Accepted)  
**Class Imbalance:** Highly imbalanced dataset (~9.6% acceptance rate)

### Data Dictionary

| Feature              | Description                                 | Type    | Range/Values                            |
| -------------------- | ------------------------------------------- | ------- | --------------------------------------- |
| `ID`                 | Customer ID                                 | Integer | 1-5000                                  |
| `Age`                | Customer age in years                       | Integer | 23-67                                   |
| `Experience`         | Years of professional experience            | Integer | -3 to 43                                |
| `Income`             | Annual income (in $000s)                    | Integer | 8-224                                   |
| `ZIPCode`            | Home address ZIP code                       | Integer | 5-digit                                 |
| `Family`             | Family size                                 | Integer | 1-4                                     |
| `CCAvg`              | Avg. credit card spending per month ($000s) | Float   | 0-10                                    |
| `Education`          | Education level (1, 2, 3)                   | Integer | 1=Undergrad, 2=Graduate, 3=Professional |
| `Mortgage`           | Value of house mortgage if any ($000s)      | Integer | 0-635                                   |
| `Personal_Loan`      | **TARGET:** Accepted personal loan?         | Binary  | 0=No, 1=Yes                             |
| `Securities_Account` | Has securities account?                     | Binary  | 0=No, 1=Yes                             |
| `CD_Account`         | Has certificate of deposit account?         | Binary  | 0=No, 1=Yes                             |
| `Online`             | Uses internet banking?                      | Binary  | 0=No, 1=Yes                             |
| `CreditCard`         | Uses credit card?                           | Binary  | 0=No, 1=Yes                             |

---

## 🎯 Project Objectives

### 1. Exploratory Data Analysis

- Understand customer demographics
- Analyze feature distributions
- Identify patterns in loan acceptance

### 2. Data Preprocessing

- Handle negative experience values
- Check for missing values
- Feature scaling and encoding
- Address class imbalance

### 3. Model Development

- Build Decision Tree classifier
- Feature importance analysis
- Model optimization
- Performance evaluation

### 4. Business Insights

- Identify high-value customer segments
- Recommend targeting strategies
- Quantify ROI improvement potential

---

## 🛠️ Technologies Used

### Core Libraries

- **Python 3.8+**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Matplotlib & Seaborn** - Visualization

### Machine Learning

- **Scikit-learn** - ML algorithms
- **Decision Trees** - Primary classification model

### Custom Toolkit

- **VKPyKit** - Personal Python package
  - `EDA` module for exploratory analysis
  - `DT` module for Decision Tree utilities

```python
from VKPyKit.EDA import *
from VKPyKit.DT import *
```

---

## 📁 Project Structure

```
P2-PersonalLoanCampaign/
├── P2_PersonalLoanCampaign_VK_Notebook_Full_Code.ipynb
├── loan_modelling.csv
└── README.md (this file)
```

---

## 🚀 How to Use

### Installation

```bash
# Install required packages
pip install pandas numpy matplotlib seaborn scikit-learn

# Install VKPyKit (custom package)
pip install vkpykit
```

### Run the Analysis

```bash
jupyter notebook P2_PersonalLoanCampaign_VK_Notebook_Full_Code.ipynb
```

---

## 📊 Analysis Workflow

```mermaid
graph LR
    A[Load Data] --> B[EDA with VKPyKit]
    B --> C[Data Cleaning]
    C --> D[Feature Engineering]
    D --> E[Train-Test Split]
    E --> F[Decision Tree Model]
    F --> G[Model Evaluation]
    G --> H[Feature Importance]
    H --> I[Business Insights]
```

---

## 🔑 Key Findings

### Customer Segmentation

**High Propensity Customers:**

- Higher income levels (Income is a strong predictor)
- Higher credit card spending (CCAvg is important)
- Specific education levels
- Certain family size demographics

**Low Propensity Customers:**

- Lower income ranges
- Minimal credit card usage
- Different banking behavior patterns

### Feature Importance

Based on Decision Tree analysis:

1. **Income** - Top predictor
2. **CCAvg** (Credit Card Average) - Strong indicator
3. **Education** - Significant factor
4. **Family Size** - Notable influence
5. **CD_Account** - Contributing factor

---

## 📈 Model Performance

**Approach:** Decision Tree Classification

**Evaluation Metrics:**

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Key Consideration:** Handling class imbalance (9.6% positive class)

---

## 💡 Business Recommendations

### 1. Targeted Marketing

Focus campaigns on customers with:

- Income > $[threshold from analysis]
- CCAvg > $[threshold from analysis]
- Specific education and family profiles

### 2. Personalized Offers

- Create tiered loan offers based on customer segments
- Customize communication based on banking behavior

### 3. Cost Optimization

- Reduce marketing spend on low-propensity segments
- Increase focus on high-propensity targets
- Expected ROI improvement: [calculated from model]

### 4. Cross-Selling Opportunities

- Leverage existing banking relationships
- Bundle loan offers with other products

---

## 📚 Skills Demonstrated

✅ **Classification modeling** with Decision Trees  
✅ **Handling imbalanced datasets**  
✅ **Feature importance analysis**  
✅ **Custom Python package usage** (VKPyKit)  
✅ **Business-focused ML** - ROI optimization  
✅ **Customer segmentation** techniques  
✅ **Model interpretation** for stakeholders

---

## 🎓 Learning Outcomes

- Building classification models for business problems
- Dealing with imbalanced datasets
- Feature engineering for financial data
- Using custom Python packages in ML workflows
- Translating model outputs to business strategies
- Decision Tree interpretation and tuning

---

## 🔧 VKPyKit Usage Example

```python
# Initialize custom modules
EDA = EDA()
DT = DT()

# Use EDA functions
EDA.plot_distributions(data)
EDA.correlation_heatmap(data)

# Use DT functions
DT.plot_tree(model, feature_names)
DT.feature_importance(model, feature_names)
```

---

## 🔗 Related Projects

- [P0: Hotel Cancellation](../P0-AIApplicationCaseStudy-HotelCancellation)
- [P1: FoodHub Analysis](../P1-FoodHub)
- [P3: EasyVisa Immigration](../P3-EnsembleLearning-Visa)

---

## 📖 Additional Resources

- [VKPyKit on PyPI](https://pypi.org/project/VKPyKit/)
- [Scikit-learn Decision Trees](https://scikit-learn.org/stable/modules/tree.html)
- [Handling Imbalanced Datasets](https://imbalanced-learn.org/)

---

## 🔗 Links

- [Back to Main Repository](../)
- [View Notebook](./P2_PersonalLoanCampaign_VK_Notebook_Full_Code.ipynb)

---

**Author:** Vishal Khapre  
**Project Type:** Binary Classification  
**Domain:** Banking & Financial Analytics  
**Tools:** Python, Scikit-learn, VKPyKit
